#!/usr/bin/python
import sys
import os
import re



add_pattern = r'''(?s)\{\+\+(?P<value>.*?)\+\+[ \t]*(\[(?P<meta>.*?)\])?[ \t]*\}'''

del_pattern = r'''(?s)\{\-\-(?P<value>.*?)\-\-[ \t]*(\[(?P<meta>.*?)\])?[ \t]*\}'''

comm_pattern = r'''(?s)\{\>\>(?P<value>.*?)\<\<\}'''

gen_comm_pattern = r'''(?s)\{[ \t]*\[(?P<meta>.*?)\][ \t]*\}'''

subs_pattern = r'''(?s)\{\~\~(?P<original>(?:[^\~\>]|(?:\~(?!\>)))+)\~\>(?P<new>(?:[^\~\~]|(?:\~(?!\~\})))+)\~\~\}'''



mark_pattern = r'''(?s)\{\=\=(?P<value>.*?)\=\=\}'''


test_pattern = '''{~~Eighty-seven~>Four score and seven~~} years ago our fathers brought forth on this continent a new {~~state~>nation~~}, conceived in liberty, and dedicated to the proposition that all men {--and women--}{>>Tackle this after the war<<} are created equal.'''



def deletionProcess(group_object):
	replaceString = ''
	if group_object.group('value') == '\n\n':
		replaceString = "<del>&nbsp;</del>"
	else:
		replaceString = '<del>' + group_object.group('value').replace("\n\n", "&nbsp;") + '</del>'
	return replaceString



def subsProcess(group_object):
	delString = '<del>' + group_object.group('original') + '</del>'
	insString  = '<ins>' + group_object.group('new') + '</ins>'
	return delString + insString


# Converts Addition markup to HTML
def additionProcess(group_object):
	replaceString = ''
	
	# Is there a new paragraph followed by new text
	if group_object.group('value').startswith('\n\n') and group_object.group('value') != "\n\n":
		replaceString = "\n\n<ins class='critic' break>&nbsp;</ins>\n\n"
		replaceString = replaceString + '<ins>' + group_object.group('value').replace("\n", " ")
		replaceString = replaceString +  '</ins>'
		
	
	# Is the addition just a single new paragraph
	elif group_object.group('value') == "\n\n":
		replaceString = "\n\n<ins class='critic break'>&nbsp;" + '</ins>\n\n'
	
	# Is it added text followed by a new paragraph?
	elif group_object.group('value').endswith('\n\n') and group_object.group('value') != "\n\n":
		replaceString = '<ins>' + group_object.group('value').replace("\n", " ") + '</ins>'
		replaceString = replaceString + "\n\n<ins class='critic break'>&nbsp;</ins>\n\n"
		
	else:
		replaceString = '<ins>' + group_object.group('value').replace("\n", " ") + '</ins>'
		

	return replaceString

def highlightProcess(group_object):
	replaceString = '<span class="critic comment">' + group_object.group('value').replace("\n", " ") + '</span>'
	return replaceString
	

def markProcess(group_object):
	replaceString = '<mark>' + group_object.group('value') + '</mark>'
	return replaceString

a = '''

<style>
	.scholmd-container {
		padding-top: 60px !important;
	}

	#criticnav {
	  position: fixed;
	  z-index: 1100;
	  top: 0;
	  left: 0;
	  width: 100%;
	  border-bottom: solid 1px #696f75;
	  margin: 0;
	  padding: 0;
	  background-color: rgba(255,255,255,0.95);
	  color: #696f75;
	  font-size: 14px;
	  font-family: "Helvetica Neue", helvetica, arial, sans-serif !important
	}

	#criticnav ul {
	  list-style-type: none;
	  width: 90%;
	  margin: 0 auto;
	  padding: 0
	}

	#criticnav ul li {
	  display: block;
	  width: 15%;
	  min-width: 100px;
	  text-align: center;
	  padding: 5px 0 3px !important;
	  margin: 5px 2px !important;
	  line-height: 1em;
	  float: left;
	  text-transform: uppercase;
	  cursor: pointer;
	  -webkit-user-select: none;
	  border-radius: 20px;
	  border: 1px solid rgba(255,255,255,0);
	  color: #777 !important
	}

	#criticnav ul li:before {
	  content: none !important
	}

	#criticnav ul li.active {
	  border: 1px solid #696f75
	}

	.original del {
		
			text-decoration: none;
	}	

	.original ins,
	.original span.popover,
	.original ins.break {
		display: none;
	}

	.edited ins {
		
			text-decoration: none;
	}	

	.edited del,
	.edited span.popover,
	.edited ins.break {
		display: none;
	}

	.original mark,
	.edited mark {
		background-color: transparent;
	}

	.markup mark {
	    background-color: #fffd38;
	    text-decoration: none;
	}

	.markup del {
	    background-color: rgba(183,47,47,0.4);
	    text-decoration: none;
	}

	.markup ins {
	    background-color: rgba(152,200,86,0.4);
	    text-decoration: none;
	}

	.markup ins.break {
		display: block;
		line-height: 2px;
		padding: 0 !important;
		margin: 0 !important;
	}

	.markup ins.break span {
		line-height: 1.5em;
	}

	.markup .popover {
		background-color: #e5b000;
		color: #fff;
	}

	.markup .popover .critic.comment {
	    display: none;
	}

	.markup .popover:hover span.critic.comment {
	    display: block;
	    position: absolute;
	    width: 200px;
	    left: 30%;
	    font-size: 0.8em; 
	    color: #ccc;
	    background-color: #333;
	    z-index: 10;
	    padding: 0.5em 1em;
	    border-radius: 0.5em;
	}

	@media print {
		#criticnav {
			display: none !important
		}
	}
}

</style>

<div id="criticnav">
<ul>
<li id="markup-button">Markup</li>
<li id="original-button">Original</li>
<li id="edited-button">Edited</li>
</ul>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<script type="text/javascript">

	function critic() {

		$('.scholmd-container').addClass('markup');
		$('#markup-button').addClass('active');
		$('ins.break').unwrap();
		$('span.critic.comment').wrap('<span class="popover" />');
		$('span.critic.comment').before('&#8225;');

	}  

	function original() {
		$('#original-button').addClass('active');
		$('#edited-button').removeClass('active');
		$('#markup-button').removeClass('active');

		$('.scholmd-container').addClass('original');
		$('.scholmd-container').removeClass('edited');
		$('.scholmd-container').removeClass('markup');
	}

	function edited() {
		$('#original-button').removeClass('active');
		$('#edited-button').addClass('active');
		$('#markup-button').removeClass('active');

		$('.scholmd-container').removeClass('original');
		$('.scholmd-container').addClass('edited');
		$('.scholmd-container').removeClass('markup');
	} 

	function markup() {
		$('#original-button').removeClass('active');
		$('#edited-button').removeClass('active');
		$('#markup-button').addClass('active');

		$('.scholmd-container').removeClass('original');
		$('.scholmd-container').removeClass('edited');
		$('.scholmd-container').addClass('markup');
	}

	var o = document.getElementById("original-button");
	var e = document.getElementById("edited-button");
	var m = document.getElementById("markup-button");

	window.onload = critic;
	o.onclick = original;
	e.onclick = edited;
	m.onclick = markup;

</script>
'''


# Accept input from Marked.app

h = sys.stdin.read()

#h = test_pattern





h = re.sub(del_pattern, deletionProcess, h, flags=re.DOTALL)

h = re.sub(add_pattern, additionProcess, h, flags=re.DOTALL)

h = re.sub(comm_pattern, highlightProcess, h, flags=re.DOTALL)

h = re.sub(mark_pattern, markProcess, h, flags=re.DOTALL)

h = re.sub(subs_pattern, subsProcess, h, flags=re.DOTALL)

# print h

z = h + a

sys.stdout.write(z)

