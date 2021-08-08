# padder
Automatically add space padding around operators. Compatiable with C++, Java, maybe more. 

![](demo-gif.gif)

## Prerequisites:
- Python (from terminal)
- Windows OS; this can certainly be applied to other OS's/setups with some modifications, but it's only been tested on Windows OS.

## Usage:

Add the following to your `.vimrc`:

`command Pad :w !python "C:\Users\gbpol\Desktop\Useful\Competitive-Programming\Util\padder.py" %:p <CR> :w<CR>`

Of course, `C:\Users\gbpol\Desktop\Useful\Competitive-Programming\Util\padder.py` should be replaced with your path to `padder.py`.

## To do:
Make this a plugin so that padding happens whenever `;` or `<enter>` is pressed, similar to some formatting extensions (like [this](https://github.com/microsoft/vscode-cpptools)). 
