# padder
Automatically add space padding around operators. Compatible with C++, Java, probably more. 

![demo](https://github.com/ar492/padder_old/blob/main/demo_gif.gif)

## Prerequisites:
- Python (from terminal)
- Windows OS; this can certainly be applied to other setups with some modifications, but it's been tested only on Windows.
- The third party [`regex` package](https://pypi.org/project/regex/)

## Usage:

Add the following to your `.vimrc`:

`command Pad :w !python "C:\Users\gbpol\Desktop\Useful\Competitive-Programming\Util\padder.py" %:p <CR> :w<CR>`

Of course, `C:\Users\gbpol\Desktop\Useful\Competitive-Programming\Util\padder.py` should be replaced with your path to `padder.py`.

## To do:
Make this a plugin so that padding happens whenever `;` or `<enter>` is pressed, similar to some formatting extensions (like [this](https://github.com/microsoft/vscode-cpptools)). 
