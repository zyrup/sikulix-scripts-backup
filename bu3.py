import subprocess;

def setClipboardData(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE);
    p.stdin.write(data);
    p.stdin.close();
    retcode = p.wait();

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

# create new window
keyDown(Key.CMD);
keyDown('n');
keyUp(Key.CMD);
keyUp('n');
wait(2);

setClipboardData('localhost/index2.php');
keyDown(Key.CMD);
keyDown('l');
keyUp(Key.CMD);
keyUp('l');
keyDown(Key.CMD);
keyDown('v');
keyUp(Key.CMD);
keyUp('v');
wait(1);
keyDown(Key.ENTER);
keyUp(Key.ENTER);
wait(3);

openDevTool();

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

# keyDown(Key.CMD);
# keyDown(Key.ALT);
# keyDown(Key.LEFT);
# keyUp(Key.CMD);
# keyUp(Key.ALT);
# keyUp(Key.LEFT);

# create new tab
keyDown(Key.CMD);
keyDown('t');
keyUp(Key.CMD);
keyUp('t');

keyDown(Key.CMD);
keyDown('l');
keyUp(Key.CMD);
keyUp('l');
keyDown(Key.CMD);
keyDown('v');
keyUp(Key.CMD);
keyUp('v');
wait(1);
keyDown(Key.ENTER);
keyUp(Key.ENTER);
wait(7);

openDevTool();

setClipboardData("""prompt('', 'var e = "'+document.querySelectorAll('.page-title em')[0].innerHTML + '";');""");
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
wait(2);

setClipboardData("decideWhatToDo(e);");
keyDown(Key.CMD);
keyDown('v');
keyUp(Key.CMD);
keyUp('v');
keyDown(Key.ENTER);
keyUp(Key.ENTER);
wait(2);

# close tab
keyDown(Key.CMD);
keyDown('w');
keyUp(Key.CMD);
keyUp('w');
wait(1);