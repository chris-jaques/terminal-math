# Terminal Math

This is a simple python script that is intended to enable you to run quick and dirty on-the-fly math expressions from your terminal without having to open anything

###Setup

#### install dependencies
```
	sudo apt-get install python3 xclip
```

#### link script to your home folder
```
	ln -s $(pwd)/terminal-math.py ~/terminal-math.py
```

#### Modify your .bashrcd
```
	nano ~/.bashrc
```
then paste in:
```
function m(){
    # Execute math function and copy results to clipboard
    python3 ~/terminal-math.py ${@:1} | xclip -sel clip;

    # Output results to terminal
    xclip -o -sel clip;
    
    # Echo for a new line
    echo "";
}
```

Now you just need to type `m` in your terminal, followed by an expression and the result will be output and copied to your clipboard


###Examples
```
m 6x2+2/4
```
outputs: 12.5

####If brackets are needed, you must use square brackets
```
m cos[pi]
```
outputs: -1

*notice* constant _pi_ is already defined as well as the cos function.


### Variables
variables begin with a `?` and are a single letter (case sensitive)
```
m ?t = 22
m 27 - ?t
```
outputs: 5

#### The most recent result of a math function is copied to your clipboard, but is also available as `??`
```
m [30/2] + 5
m 2 + ??
```
outputs 22

```
m 2+2
m 2x??
m ?? + ??
```
outputs 16


### Other Commands

#### Clear the variable cache
```
m c
```

#### Display the current variable cache
```
m v
```