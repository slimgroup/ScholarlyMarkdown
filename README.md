# Official SLIM internal distribution of ScholarlyMarkdown

CLI interface to ScholaryMarkdown converter. In order to use the converter, you will need to add the `bin` folder to your path and to setup
`SCHOLMD_PATH` to the root of this directory to setup the different paths to templates and style files. From this root directory you can run

```bash
echo "export SCHOLMD_PATH=$PWD" >> ~/.bashrc  # or ~/.zshrc for zsh shelss
echo "export PATH=$PATH:$PWD/bin" >> ~/.bashrc # or ~/.zshrc for zsh shelss
```

ScholPandocConverter is a shell script that follows the selection path from the drop-on Mac application for now. Run it without any arguments to get the syntax info.

You can find the documentation and syntax guide for ScholarlyMarkdown at: [Documentation](http://scholarlymarkdown.com/)

The converter (`scholdoc`) is the utility that converts the ScholarlyMarkdown document and is documented [here](http://scholdoc.scholarlymarkdown.com/). The usage is fairly simple. Once you have a markdown file written with ScholarlyMarkdown, simply run `ScholPandocConverter myfile.md` and you will have a selection menu to choose from for the output file you want.


## Coming up

We will add the drop-on Mac application that allows to drag a markdown file onto the app to access a GUI extension of the converter.

## Author

This software was developed at the University of British Columbia by Tim Y. Lin during his PhD in the [SLIM group](https://slim.gatech.edu/).