import subprocess;

def setClipboardData(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()

def openDevTool():
    keyDown(Key.CMD);
    keyDown(Key.ALT);
    keyDown('i');
    keyUp(Key.CMD);
    keyUp(Key.ALT);
    keyUp('i');
    wait(1);
    keyDown(Key.TAB);
    keyUp(Key.TAB);

def closeDevTool():
    keyDown(Key.CMD);
    keyDown(Key.ALT);
    keyDown('i');
    keyUp(Key.CMD);
    keyUp(Key.ALT);
    keyUp('i');
    wait(1);

openApp("Google Chrome");

#reload page
keyDown(Key.CMD);
keyDown('r');
keyUp(Key.CMD);
keyUp('r');

openDevTool();

# run fetchNextArticleId()
setClipboardData('fetchNextArticleId()');
keyDown(Key.CMD);
keyDown('v');
keyUp(Key.CMD);
keyUp('v')
keyDown(Key.ENTER);
keyUp(Key.ENTER);
wait(1);
keyDown(Key.CMD);
keyDown('c');
keyUp(Key.CMD);
keyUp('c');
wait(1);
keyDown(Key.ENTER);
keyUp(Key.ENTER);
wait(1);

# create new tab
keyDown(Key.CMD);
keyDown('t');
keyUp(Key.CMD);
keyUp('t');

# google for value
keyDown(Key.CMD);
keyDown('v');
keyUp(Key.CMD);
keyUp('v');
keyDown(Key.ENTER);
keyUp(Key.ENTER);
wait(1);

openDevTool();

# access first google link
setClipboardData("prompt('', document.querySelectorAll('h3.r a')[0].href);");
keyDown(Key.CMD);
keyDown('v');
keyUp(Key.CMD);
keyUp('v');
keyDown(Key.ENTER);
keyUp(Key.ENTER);
wait(1);

# copy text
keyDown(Key.CMD);
keyDown('c');
keyUp(Key.CMD);
keyUp('c');
keyDown(Key.ENTER);
keyUp(Key.ENTER);

# open apparent site url in same tab
keyDown(Key.CMD);
keyDown('l');
keyUp(Key.CMD);
keyUp('l');
keyDown(Key.CMD);
keyDown('v');
keyUp(Key.CMD);
keyUp('v')
wait(1);
keyDown(Key.ENTER);
keyUp(Key.ENTER);
wait(5);

closeDevTool();
openDevTool();

# access apparent site 404 page
setClipboardData("""prompt('', 'var e = "' + document.querySelectorAll('.intro__main-title')[0].className + '"');""");
keyDown(Key.CMD);
keyDown('v');
keyUp(Key.CMD);
keyUp('v');
keyDown(Key.ENTER);
keyUp(Key.ENTER);
wait(1);

# copy text
keyDown(Key.CMD);
keyDown('c');
keyUp(Key.CMD);
keyUp('c');
keyDown(Key.ENTER);
keyUp(Key.ENTER);

# close tab
keyDown(Key.CMD);
keyDown('w');
keyUp(Key.CMD);
keyUp('w');
wait(1);

# temporary storage
keyDown(Key.CMD);
keyDown('v');
keyUp(Key.CMD);
keyUp('v');
keyDown(Key.ENTER);
keyUp(Key.ENTER);
wait(1);

setClipboardData("decideWhatToDo(e);");
keyDown(Key.CMD);
keyDown('v');
keyUp(Key.CMD);
keyUp('v');
keyDown(Key.ENTER);
keyUp(Key.ENTER);
wait(1);

closeDevTool();



