%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% This is file cph18.cls'  %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
%% Made by: Bobby Hak
%% Email: bobby.hak@cgg.com
%%
%% This class has been tested with:
%%     MiKTeX version 2.9
%%
%% It is based on the standard LaTeX2e "article" class and some
%% standard packages:
%%    times    - for the font Times New Roman, 11pt
%%    mathptmx - for the font Times New Romen with math support
%%    fancyhdr - for defining headnote and footnote
%%    graphicx - for including logo
%%    natbib   - for referencing
%%
%% All packages should be availble in any normal distribution of LaTeX,
%% or can be downloaded from the CTAN homepage:
%%    www.ctan.org
%%
%% Changelog v1.0 -> v1.1
%% - Bibliography font to 11pt
%% - Reduce white space between lines (50 -> 55 lines per page)
%%
\NeedsTeXFormat{LaTeX2e}[1996/12/01]
\ProvidesClass{cph18}[2015/05/28 v1.1 EAGE Abstract Class]
%%
%% Pass all options directly to 'article'
%%
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
%%
%% prefered fontsize, papersize, and type
%%
\LoadClass[oneside,11pt,a4paper]{article}
%%
%% prefered fonts: Times New Roman becomes the standard font (text)
%%
\RequirePackage[T1]{fontenc}
\RequirePackage{times}
\RequirePackage{mathptmx}
\linespread{0.92}
%%
%% Page size formats / 1in ~ 72pt, 1pt ~ 03515mm
%%
\setlength{\hoffset}{-1.0in}
\setlength{\oddsidemargin}{1.0in}
\setlength{\voffset}{-1.0in}
\setlength{\topmargin}{0.15in}
\setlength{\headheight}{0.75in}
\setlength{\headsep}{0.1in}
\setlength{\textheight}{9.7in}
\setlength{\paperheight}{11.7in}
\setlength{\textwidth}{6.27in}
\setlength{\paperwidth}{8.27in}
\setlength{\footskip}{0.51in}
\addtolength{\footskip}{-1.0\baselineskip}
%%
%% some others
%%
\setcounter{secnumdepth}{0} % no numbering of sections
\setlength{\parindent}{0pt} % no indent for new paragraphs
\setlength{\parskip}{\baselineskip} % skip one line between paragraphs
\setlength{\partopsep}{0pt} % skip between environments and paragraphs
\setlength{\topsep}{0pt} % skip between environments and paragraphs
%%
%% bibliography
%%
\RequirePackage{natbib} % special citing commands
\setlength{\bibsep}{0pt} % no lines between bibitems
\setlength{\bibhang}{1em} % indentation of second line in bibitem
\bibliographystyle{firstbreak} % stylefile
%%
%% set header and footer
%%
\RequirePackage{fancyhdr}
\RequirePackage{graphicx}
\pagestyle{fancy} % load package
\fancyhf{} % clear any existing styles
\fancyhead[R]{\includegraphics[width=1.66in]{cph18.eps}} % input logo top right, even and odd side, in margin
\fancyfoot[C]{{\fontsize{10}{8}\selectfont{%
\vspace*{-2pt}
80\textsuperscript{th} EAGE Conference \& Exhibition 2018\\\vspace{-2pt}
11--14 June 2018, Copenhagen, Denmark}}} % footnote
\renewcommand{\headrulewidth}{0pt} % no line in header
\renewcommand{\footrulewidth}{0.5pt} % add line in footnote
\pagenumbering{gobble} % define page numbering
%%
%% section headers and paragraphs
%%
\renewcommand{\section}{\@startsection{section}%
{1}% level
{0pt}% indent
{.1ex plus -.1ex}% beforeskip
{.1ex plus -.1ex}% afterskip
{\fontsize{11}{11}\selectfont\bf}} % font
%
\renewcommand{\subsection}{\@startsection{subsection}%
{2}% level
{0pt}% indent
{.1ex plus -.1ex}% beforeskip
{.1ex plus -.1ex}% afterskip
{\fontsize{11}{11}\selectfont\emph}} % font
%%
%% caption font
%%
\long\def\@makecaption#1#2{%
  \vskip\abovecaptionskip
  \sbox\@tempboxa{{\bf\itshape #1} \itshape #2}%
  \ifdim \wd\@tempboxa >\hsize
    {{\bf\itshape #1} \itshape #2\par}
  \else
    \hbox to\hsize{\hfil\box\@tempboxa\hfil}%
  \fi
  \vskip\belowcaptionskip}
% EOF
