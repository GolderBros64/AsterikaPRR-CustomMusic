import customtkinter
import asterikamdEncrypt
import shutil
import subprocess
import threading
import json
import sys
from winotify import Notification, audio
from pathlib import Path

if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).resolve().parent
else:
    BASE_DIR = Path(__file__).resolve().parent
    
ctk = customtkinter
canRestore = False
isModded = False
canBak = False
isBacking = False
#npx.cmd @electron/asar extract .\resources\app.asar .\app_clean

app = ctk.CTk()
app.title("AsterikaCustomMusicInsertHelper - v1.0 - ManageSongs.js for Asterika V1.0.3.11")
app.geometry("900x450")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
container = ctk.CTkFrame(app, fg_color="transparent")
container.pack(expand=True)


frame = ctk.CTkFrame(container,corner_radius=15,border_width=5,border_color="#E05D7B",width=266)
frame.pack(padx=20, pady=(20,5),side="left")
frame2 = ctk.CTkFrame(container,corner_radius=15,border_width=5,border_color="#26334E",width=266)
frame2.pack(padx=20, pady=(20,5),side="left")
frame3 = ctk.CTkFrame(container,corner_radius=15,border_width=5,border_color="#E47C5B",width=266)
frame3.pack(padx=20, pady=(20,5),side="left")
frame4 = ctk.CTkFrame(container,corner_radius=15,border_width=5,border_color="#E47C5B",width=340)
frame4.pack(padx=20, pady=(20,5),side="left",fill="x")

#Frame

label = ctk.CTkLabel(frame, text="Song Internal ID", fg_color="#5831C3",corner_radius=20,font=("",20))
label.pack(pady=(20,5),padx=10)

entry = ctk.CTkEntry(frame, placeholder_text="Song Internal ID...",fg_color="#2A2A24")
entry.pack(pady=5,padx=40)

labela = ctk.CTkLabel(frame, text="Music File (.ogg)", fg_color="#5831C3",corner_radius=20,font=("",20))
labela.pack(pady=5,padx=10)

entrya = ctk.CTkEntry(frame, placeholder_text="Music File (.ogg)",fg_color="#2A2A24")
entrya.pack(pady=5,padx=40)

labelb = ctk.CTkLabel(frame, text="Music Preview File (.ogg)", fg_color="#5831C3",corner_radius=20,font=("",20))
labelb.pack(pady=5,padx=10)

entryb = ctk.CTkEntry(frame, placeholder_text="Music Preview File (.ogg)",fg_color="#2A2A24")
entryb.pack(pady=5,padx=40)

labelc = ctk.CTkLabel(frame, text="Music icon Image", fg_color="#5831C3",corner_radius=20,font=("",20))
labelc.pack(pady=5,padx=10)

entryc = ctk.CTkEntry(frame, placeholder_text="Music icon...",fg_color="#2A2A24")
entryc.pack(pady=(5,15),padx=40)

label5 = ctk.CTkLabel(frame, text="Chart to Package (Optional)", fg_color="#E47C5B",corner_radius=20,font=("",16))
label5.pack(pady=5,padx=10)
entry5 = ctk.CTkEntry(frame, placeholder_text="filename.asterika",fg_color="#2A2A24")
entry5.pack(pady=(5,10),padx=40)
#----
#Frame2
label2 = ctk.CTkLabel(frame2, text="Game install Location", fg_color="#26334E",corner_radius=20,font=("",20))
label2.pack(pady=(20,5),padx=10)
entry2 = ctk.CTkEntry(frame2, placeholder_text="Location... (C:\\)",fg_color="#2A2A24",width=248)
entry2.pack(pady=5,padx=40)
#----
#Frame3
#title,enname(opt),id,artist,composer(op),path(?),bpm,readybeats,tracklenght(in s),endbeat,initialdelay(in s)
label3 = ctk.CTkLabel(frame3, text="Title", fg_color="#E47C5B",corner_radius=20,font=("",16))
label3.pack(pady=5,padx=10)
entry3 = ctk.CTkEntry(frame3, placeholder_text="title...",fg_color="#2A2A24")
entry3.pack(pady=5,padx=40)

label3a = ctk.CTkLabel(frame3, text="En Title (Optional)", fg_color="#E47C5B",corner_radius=20,font=("",16))
label3a.pack(pady=5,padx=10)
entry3a = ctk.CTkEntry(frame3, placeholder_text="title...",fg_color="#2A2A24")
entry3a.pack(pady=5,padx=40)

label3b = ctk.CTkLabel(frame3, text="Artist", fg_color="#E47C5B",corner_radius=20,font=("",16))
label3b.pack(pady=5,padx=10)
entry3b = ctk.CTkEntry(frame3, placeholder_text="artist",fg_color="#2A2A24")
entry3b.pack(pady=5,padx=40)

label3c = ctk.CTkLabel(frame3, text="Composer (Optional)", fg_color="#E47C5B",corner_radius=20,font=("",16))
label3c.pack(pady=5,padx=10)
entry3c = ctk.CTkEntry(frame3, placeholder_text="composer...",fg_color="#2A2A24")
entry3c.pack(pady=5,padx=40)

label3d = ctk.CTkLabel(frame3, text="BPM", fg_color="#E47C5B",corner_radius=20,font=("",16))
label3d.pack(pady=5,padx=10)
entry3d = ctk.CTkEntry(frame3, placeholder_text="Integer",fg_color="#2A2A24")
entry3d.pack(pady=5,padx=40)

label3e = ctk.CTkLabel(frame3, text="Ready Beats", fg_color="#E47C5B",corner_radius=20,font=("",16))
label3e.pack(pady=5,padx=10)
entry3e = ctk.CTkEntry(frame3, placeholder_text="Integer",fg_color="#2A2A24")
entry3e.pack(pady=5,padx=40)

label3f = ctk.CTkLabel(frame3, text="Song Lenght (in Seconds)", fg_color="#E47C5B",corner_radius=20,font=("",16))
label3f.pack(pady=5,padx=10)
entry3f = ctk.CTkEntry(frame3, placeholder_text="seconds...",fg_color="#2A2A24")
entry3f.pack(pady=5,padx=40)

label3g = ctk.CTkLabel(frame3, text="End Beat", fg_color="#E47C5B",corner_radius=20,font=("",16))
label3g.pack(pady=5,padx=10)
entry3g = ctk.CTkEntry(frame3, placeholder_text="Integer",fg_color="#2A2A24")
entry3g.pack(pady=5,padx=40)

label3h = ctk.CTkLabel(frame3, text="Initial Delay (in Seconds)", fg_color="#E47C5B",corner_radius=20,font=("",16))
label3h.pack(pady=5,padx=10)
entry3h = ctk.CTkEntry(frame3, placeholder_text="seconds...",fg_color="#2A2A24")
entry3h.pack(pady=5,padx=40)

#----
#Frame4
#difficultyTagging(make this easier)
#'difficultyTagging': {'1': {'tags': ['HighSpeed','VeryBusy'],'level': 15},'2': {'tags': ['HighSpeed','VeryBusy'],'level': 23},'3': {'tags': ['HighSpeed','VeryBusy'],'level': 28},'4': {'tags': ['HighSpeed','VeryBusy'],'level': 31}

label4 = ctk.CTkLabel(frame4, text="Difficulty & Tags", fg_color="#E47C5B",corner_radius=20,font=("",16))
label4.pack(pady=(10,5),padx=10)
label4a = ctk.CTkLabel(frame4, text="Standard", fg_color="#3AB76B",corner_radius=20,font=("",16))
label4a.pack(pady=5,padx=10)
row = ctk.CTkFrame(frame4, fg_color="transparent")
row.pack(pady=5,fill="x",padx = 7)
rowa = ctk.CTkFrame(frame4, fg_color="transparent")
rowa.pack(pady=5,fill="x",padx = 7)

label4b = ctk.CTkLabel(frame4, text="Master", fg_color="#DD9C19",corner_radius=20,font=("",16))
label4b.pack(pady=5,padx=10)
row2 = ctk.CTkFrame(frame4, fg_color="transparent")
row2.pack(pady=5,fill="x",padx = 7)
row2a = ctk.CTkFrame(frame4, fg_color="transparent")
row2a.pack(pady=5,fill="x",padx = 7)

label4c = ctk.CTkLabel(frame4, text="Phantom", fg_color="#DC1A80",corner_radius=20,font=("",16))
label4c.pack(pady=5,padx=10)
row3 = ctk.CTkFrame(frame4, fg_color="transparent")
row3.pack(pady=5,fill="x",padx = 7)
row3a = ctk.CTkFrame(frame4, fg_color="transparent")
row3a.pack(pady=5,fill="x",padx = 7)

label4d = ctk.CTkLabel(frame4, text="Nightmare", fg_color="#0D1AC3",corner_radius=20,font=("",16))
label4d.pack(pady=5,padx=10)
row4 = ctk.CTkFrame(frame4, fg_color="transparent")
row4.pack(pady=5,fill="x",padx = 7)
row4a = ctk.CTkFrame(frame4, fg_color="transparent")
row4a.pack(pady=(5,15),fill="x",padx = 7)

#----------
#Song labels Declarations
labelF4 = ctk.CTkLabel(row, text="Tags:")
labelF4.pack(side="left", padx=5)
entryF4 = ctk.CTkEntry(row, placeholder_text="tag1,tag2,etc")
entryF4.pack(side="left")

labelF4a = ctk.CTkLabel(rowa, text="Level:")
labelF4a.pack(side="left", padx=5)
entryF4a = ctk.CTkEntry(rowa, placeholder_text="Integer",fg_color="#2A2A24")
entryF4a.pack(side="left")

label2F4 = ctk.CTkLabel(row2, text="Tags:")
label2F4.pack(side="left", padx=5)
entry2F4 = ctk.CTkEntry(row2, placeholder_text="tag1,tag2,etc")
entry2F4.pack(side="left")

label2F4a = ctk.CTkLabel(row2a, text="Level:")
label2F4a.pack(side="left", padx=5)
entry2F4a = ctk.CTkEntry(row2a, placeholder_text="Integer",fg_color="#2A2A24")
entry2F4a.pack(side="left")

label3F4 = ctk.CTkLabel(row3, text="Tags:")
label3F4.pack(side="left", padx=5)
entry3F4 = ctk.CTkEntry(row3, placeholder_text="tag1,tag2,etc")
entry3F4.pack(side="left")

label3F4a = ctk.CTkLabel(row3a, text="Level:")
label3F4a.pack(side="left", padx=5)
entry3F4a = ctk.CTkEntry(row3a, placeholder_text="Integer",fg_color="#2A2A24")
entry3F4a.pack(side="left")

label4F4 = ctk.CTkLabel(row4, text="Tags:")
label4F4.pack(side="left", padx=5)
entry4F4 = ctk.CTkEntry(row4, placeholder_text="tag1,tag2,etc")
entry4F4.pack(side="left")

label4F4a = ctk.CTkLabel(row4a, text="Level:")
label4F4a.pack(side="left", padx=5)
entry4F4a = ctk.CTkEntry(row4a, placeholder_text="Integer",fg_color="#2A2A24")
entry4F4a.pack(side="left")
#----------

def notifmain(notif:str="Looping.Alarm4",titlea:str="Luigi!",info:str="You've got mail",isFolder:bool=False,folder:str=entry2.get(),isGame:bool=False):
    toast = Notification(app_id="Asterika Music Modding",title=titlea,msg=info,duration="short")
    if isFolder:
        toast.add_actions(
            label="Open Folder",
            launch=Path(folder)
        )

    if isGame:
        print("unused functionality bc i can't launch the exe directly oh well shi----")

    toast.set_audio(audio.Sound(f"ms-winsoundevent:Notification.{notif}"), loop=False)
    #audio.Reminder, LoopingAlarm2,LoopingAlarm3,LoopingAlarm4,
    #                                            ^^^
    toast.show()

def notif1(title:str="Luigi Number One",info:str="You've got mail",kibi:bool=False,folda:str=entry2.get()):
    notifmain("Looping.Alarm4",title,info,kibi,folda)

def animate_button(button):
    original_width = button.cget("width")
    original_height = button.cget("height")

    # Shrink
    button.configure(
        width=original_width - 10,
        height=original_height - 4
    )

    # Grow back
    button.after(60, lambda: button.configure(
        width=original_width,
        height=original_height
    ))

def backupbutton():
    threading.Thread(target=backupbutton_thread, daemon=True).start()

def backupbutton_thread():
    global canRestore,canBak,isBacking,BASE_DIR
    isBacking = True
    app.after(0, lambda: button2.configure(state="disabled"))
    canBak = False
    subprocess.run([
        "npx.cmd",
        "@electron/asar",
        "extract",
        r".\resources\app.asar",
        r".\app_clean"
    ], cwd=entry2.get(), check=True)
    subprocess.run([
        "npx.cmd",
        "@electron/asar",
        "extract",
        r".\resources\app.asar",
        r".\app_mod"
    ], cwd=entry2.get(), check=True)
    file = BASE_DIR / "manage-song.js"
    shutil.copy2(file,entry2.get())
    isBacking = False
    canRestore = True
    notif1("Succesfully Backed Up game Data","You can now Proceed with modding!")

def EncryptSongBT():
    global BASE_DIR
    out = BASE_DIR / "EncryptedSongs" / (entry.get() + ".jpg")
    outa = BASE_DIR / "EncryptedSongs" / (entry.get()+".asterika")
    encrypted_dir = BASE_DIR / "EncryptedSongs"
    try:
        asterikamdEncrypt.Encrypt(entrya.get(),entry.get(),False,output_dir=encrypted_dir)
        asterikamdEncrypt.Encrypt(entryb.get(),entry.get(),True,output_dir=encrypted_dir)
        shutil.copy2(BASE_DIR / entryc.get(), out)
        shutil.copy2(BASE_DIR / entry5.get(),outa)
        notif1("Succesfully Encripted Song: "+entry.get(),"Files in: "+str(BASE_DIR / "EncryptedSongs"),True,str(BASE_DIR / "EncryptedSongs"))
    except Exception as e:
        print(f"Error: {e}")
        notif1(f"An Error occured while Encrypting Song: {type(e).__name__}","Please Check the console for the full error")

def restoregame():
    subprocess.run([
        "npx.cmd",
        "@electron/asar",
        "pack",
        "app_clean",
        "app_clean.asar"
    ], cwd=entry2.get(), check=True)
    shutil.copy2(Path(entry2.get())/"app_clean.asar",Path(entry2.get())/"resources"/"app.asar")
    notif1("Successfully Restored game from 'app_clean'","If not just use 'Check file integrity' on Steam",True)


isRemoving = False
def removeEntry():
    global isRemoving
    try:
        isRemoving = True
        buttonEntryRM.configure(state="disabled")
        subprocess.run([
            "node",
            "manage-song.js",
            "remove",
            entry.get()
        ], cwd=entry2.get(), check = True)
        isRemoving = False
        buttonEntryRM.configure(state="enabled")
        notif1(f"Successfully removed entry for '{entry.get()}'!","(Or entry not Found)")
    except Exception as e:
        print(f"Error: {e}")
        notif1(f"An Error occured while Removing Entry: {type(e).__name__}","Please Check the console for the full error")

isEntrying = False
def insertEntry():
    global isEntrying
    isEntrying = True
    try:
        buttonEntry.configure(state="disabled")
        songEntry = {
            "title": entry3.get(),
            "enName": entry3a.get(),
            "id": entry.get(),
            "artist": entry3b.get(),
            "composer": entry3c.get(),
            "bpm": int(entry3d.get()),
            "readyBeats": int(entry3e.get()),
            "trackLength": float(entry3f.get()),
            "endBeat": int(entry3g.get()),
            "initialDelay": float(entry3h.get()),
            "difficultyTagging": {
                "1": {
                    "tags": [tag.strip() for tag in entryF4.get().split(",") if tag.strip()],
                    "level": int(entryF4a.get())
                },
                "2": {
                   "tags": [tag.strip() for tag in entry2F4.get().split(",") if tag.strip()],
                   "level": int(entry2F4a.get())
                },
                "3": {
                    "tags": [tag.strip() for tag in entry3F4.get().split(",") if tag.strip()],
                    "level": int(entry3F4a.get())
                },
                "4": {
                    "tags": [tag.strip() for tag in entry4F4.get().split(",") if tag.strip()],
                    "level": int(entry4F4a.get())
                }
            }
        }
        subprocess.run([
            "node",
            "manage-song.js",
            "add",
            songEntry["id"],
            json.dumps(songEntry)
        ], cwd=entry2.get(), check = True)
        isEntrying = False
        buttonEntry.configure(state="enabled")
        notif1(f"Successfully added entry for '{songEntry["id"]}'!","")
    except Exception as e:
        print(f"Error: {e}")
        notif1(f"An Error occured while Adding Entry: {type(e).__name__}","Please Check the console for the full error")

def insertfiles():
    global BASE_DIR
    buttonFiles.configure(state="disabled")
    buttonFilesRM.configure(state="disabled")
    idl = entry.get()
    dest = Path(entry2.get()) / "app_mod" / "out" / "renderer" / "music" / "custom"
    dest.mkdir(parents=True, exist_ok=True)
    out = Path(entry2.get()) / "app_mod" / "out" / "renderer" / "music" / "custom"
    try:
        shutil.copy2(BASE_DIR / "EncryptedSongs" / f"{idl}.asterikamd",out) #MusicFile
        shutil.copy2(BASE_DIR / "EncryptedSongs" / f"{idl}.preview.asterikamd",out) #MusicPreviewFile
        shutil.copy2(BASE_DIR / "EncryptedSongs" / f"{idl}.jpg",out) #MusicIconFile
        if (BASE_DIR / "EncryptedSongs" / f"{idl}.asterika").is_file():
            shutil.copy2(BASE_DIR / "EncryptedSongs" / f"{idl}.asterika",out)
        else:
            print(f"Song {idl} doesn't have a chart packaged! song will show up but won't be playable. proceeding")
        notif1("Successfully Inserted Files for "+idl,"Remember to Patch the Game first!",True)
    except FileNotFoundError:
        notif1("One or More Files you were trying to Add are missing!","Check the 'EncryptedSongs' Folder for the files",True,str(BASE_DIR / "EncryptedSongs"))

def removefiles():
    buttonFiles.configure(state="disabled")
    buttonFilesRM.configure(state="disabled")
    idl = entry.get()
    dest = Path(entry2.get()) / "app_mod" / "out" / "renderer" / "music" / "custom"
    dest.mkdir(parents=True, exist_ok=True)
    out = Path(entry2.get()) / "app_mod" / "out" / "renderer" / "music" / "custom"
    try:
        (out / f"{idl}.asterikamd").unlink()
        (out / f"{idl}.preview.asterikamd").unlink()
        (out / f"{idl}.jpg").unlink()
        (out / f"{idl}.asterika").unlink(missing_ok=True)
        notif1(f"Files Successfully removed for '{idl}'!","",True,str(out))
    except FileNotFoundError:
        notif1("One or More Files you were trying to remove are missing!","Check the 'custom' Folder for the files",True,str(out))


def packgame():
    buttonPatch.configure(state="disabled")
    try:
        buttonPatch.configure(state="disabled")
        subprocess.run([
            "npx.cmd",
            "@electron/asar",
            "pack",
            "app_mod",
            "app_mod.asar"
        ], cwd=entry2.get(), check=True)
        shutil.copy2(Path(entry2.get())/"app_mod.asar",Path(entry2.get())/"resources"/"app.asar")
        notif1("Successfully patched the Game!","Check if your songs are in it.")
    except Exception as e:
        print(f"Error: {e}")
        notif1(f"An Error occured while Patching game: {type(e).__name__}","Please Check the console for the full error\n(are we cooked?)")

button = customtkinter.CTkButton(frame, text="Encrypt Song", command=EncryptSongBT,fg_color="#E05D7B",hover_color="#FF94AC")
button.pack(pady=(10,10))

button2 = customtkinter.CTkButton(frame2, text="Backup Game", command=backupbutton,fg_color="#26334E",hover_color="#455B78",state="disabled")
button2.pack(pady=(10,10))

button2a = customtkinter.CTkButton(frame2, text="Restore Clean Game", command=restoregame,fg_color="#263384",hover_color="#4E65B4",state="disabled")
button2a.pack(pady=(5,10))

buttonPatch = customtkinter.CTkButton(frame2, text="Patch Game", command=packgame,fg_color="#26334E",hover_color="#455B78",state="disabled")
buttonPatch.pack(pady=(5,10))

buttonEntryRM = customtkinter.CTkButton(frame4, text="Remove Entry", command=lambda:[animate_button(buttonEntryRM), removeEntry()],fg_color="#DD9C19",hover_color="#DDC79C",state="disabled")
buttonEntryRM.pack(pady=(10,10))

buttonEntry = customtkinter.CTkButton(frame4, text="Insert Entry", command=lambda:[animate_button(buttonEntry), insertEntry()],fg_color="#DD9C19",hover_color="#DDC79C",state="disabled")
buttonEntry.pack(pady=(10,10))

buttonFiles = customtkinter.CTkButton(frame4, text="Insert Files", command=insertfiles,fg_color="#DC1A80",hover_color="#DD9AC1",state="disabled")
buttonFiles.pack(pady=(5,5))
buttonFilesRM = customtkinter.CTkButton(frame4, text="Remove Files", command=removefiles,fg_color="#DC1A80",hover_color="#DD9AC1",state="disabled")
buttonFilesRM.pack(pady=(5,10))

def checkEntry():
    global isEntrying,isRemoving,isModded
    buttonEntryRM.configure(state="enabled")
    if any(not lugi.get() for lugi in [entry,entry3,entry3b,entry3d,entry3e,entry3f,entry3g,entry3h]) and (not isEntrying):
        buttonEntry.configure(state="disabled")
        if not entry.get() and not isRemoving:
            buttonEntryRM.configure(state="disabled")
    else:
        buttonEntry.configure(state="enabled")

    if not isModded:
        buttonEntryRM.configure(state="disabled")
        buttonEntry.configure(state="disabled")
    
    if not (entry.get()) or not (entry2.get()):
        buttonFiles.configure(state="disabled")
        buttonFilesRM.configure(state="disabled")
    else:
        buttonFiles.configure(state="enabled")
        buttonFilesRM.configure(state="enabled")

    app.after(1000, checkEntry)

def check_folder():
    global canRestore, isModded, canBak, isBacking,isEntrying,isRemoving
    isModded = False
    path = entry2.get()
    if path and Path(path).is_dir():
        path = Path(path)
        if (path / "app_clean").exists() and (path / "app_mod").exists():
            canRestore = True
            isModded = True
            canBak = False
        else:
            isModded = False
            if (path / "resources" / "app.asar").exists():
                canBak = True
            else:
                canBak = False
    else:
        canBak = False
        button2.configure(state="disabled")

    if canRestore and isModded:
        button2a.configure(state="enabled")
    else:
        button2a.configure(state="disabled")

    if canBak and not isBacking:
        button2.configure(state="enabled")
    else:
        button2.configure(state="disabled")

    if isModded and (not isBacking) and (not isEntrying) and (not isRemoving):
        buttonPatch.configure(state="enabled")
    else:
        buttonPatch.configure(state="disabled")

    app.after(250, check_folder)


check_folder()
checkEntry()

app.mainloop()