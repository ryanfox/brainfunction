Brainfunction
=============

You know how C++ was "C with classes"?  You might say brainfunction is "brainfuck with functions".

Brainfunction takes the standard brainfuck language, and adds several features, granting immense power to the
brainfunction developer.  The standard eight brainfuck symbols are:

* `+` increment the current cell's value
* `-` decrement the current cell's value
* `<` move the cell pointer left
* `>` move the cell pointer right
* `[` start a loop
* `]` end a loop
* `,` read a byte
* `.` print a byte

To this, brainfunction adds the concept of functions.  Each line of text in a brainfunction source file is a function.
Thus, the brain (brainfunction VM) has a vertical array of functions, in addition to the horizontal array of cells.
Functions can call other functions, and return values.

To accomodate this eye-popping featureset, brainfunction incorporates four new symbols. Brainfunction's symbols are:

* `^` move the function pointer up
* `v` move the function pointer down
* `:` call the function currently pointed to
* `;` return the value in the cell pointed to by the cell pointer

#### Example
Here's a hello world, brainfunction-style.

    v:vv:^^:vv:^:v:^:v:^:vv:
    >++++++++++[>++++++++++<-]>++++.---.+++++++..+++.                    print hello
    >++++++++++++[>++++++++++<-]>-.--------.+++.------.--------.         print world
    >++++[>++++++++<-]>.                                                 print space character
    >++++[>++++++++<-]>+.                                                print !

When evaluated, this will print

    hello hello world world world!


## Usage
python brainfunction.py source_file.b


## Functions
Functions in brainfunction are defined to be one line of text.  "Wait a minute, I like to add newlines to my code to
split it into logical sections!" you say.  Oh, sorry, you were looking for an easy-to-use language?  You must have
us confused for [someone](https://www.python.org/) [else](https://www.ruby-lang.org/en/).  "B-b-but my comments have
the letter v in them!"  Just like many other languages, `;` ends a line.  If that is the last instruction in your
function proper, any remaining characters will be unreachable.

Evaluation always starts with the first function in a file, and continues until that function terminates or an error
is encountered.


#### Calling functions
To call a function, use the symbol `:`.  The function currently pointed to by the function pointer will be called.
The value in the current cell will be passed to it as an argument.  This argument is placed in cell 0 of the callee.
Whatever value the callee returns will be placed in the current cell, *gasp* overwriting the previous value.  Cf.
previous section if section if this causes you consternation.

The function pointer, instruction pointer, and code pointer all initialized to 0.

#### Returning values
There are two ways to return a value in brainfunction: either the return symbol, `;`, or when the end of the function
is reached.  In either case, the value of the cell currently pointed to by the cell pointer is returned.  You can
remember the return symbol because it looks like function call but the bottom dot is going back.
(Returning!  Get it?...  I'll see myself out.)

## Roadmap
I'm not sure what the next version of brainfunction will look like, but I'm definitely naming it higher-brainfunction.
Maybe better error messages, maybe a debugger.

Writeup can be found at
[https://foxrow.com/brainfunction-brainfuck-with-functions/](https://foxrow.com/brainfunction-brainfuck-with-functions/)