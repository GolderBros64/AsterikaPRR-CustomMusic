const fs = require("fs");

const file = ".\\app_mod\\out\\renderer\\assets\\index-CzdpGZJ0.js";

const command = process.argv[2];
const songId = process.argv[3];
const songJson = process.argv[4];

if (!command || !songId) {
    console.log("Usage:");
    console.log("  node manage-song.js add <songId> <songData>");
    console.log("  node manage-song.js remove <songId>");
    process.exit(1);
}

let song;

if (command === "add") {
    if (!songJson) {
        console.error("Song data missing.");
        process.exit(1);
    }

    try {
        song = JSON.parse(songJson);
    }
    catch (error) {
        console.error("Invalid song JSON.");
        process.exit(1);
    }
}

if (!command || !songId) {
    console.log("Usage:");
    console.log("  node manage-song.js add <songId>");
    console.log("  node manage-song.js remove <songId>");
    process.exit(1);
}

const data = fs.readFileSync(file);

const marker = Buffer.from("const MUSIC_MANIFEST=[", "ascii");
const markerPos = data.indexOf(marker);

if (markerPos === -1) {
    throw new Error("MUSIC_MANIFEST not found.");
}

const insertPos = markerPos + marker.length;

if (command === "add") {

    const difficultyTagging =
    JSON.stringify(song.difficultyTagging)
        .replace(/"/g, "'");

    const entry = Buffer.from(
        `{'title':'${song.title}',` +
        `'enName':'${song.enName}',` +
        `'id':'${songId}',` +
        `'artist':'${song.artist}',` +
        `'composer':'${song.composer}',` +
        `'path':'music/custom/${songId}',` +
        `'chart':{` +
            `'bpm':${song.bpm},` +
            `'readyBeats':${song.readyBeats},` +
            `'trackLength':${song.trackLength},` +
            `'endBeat':${song.endBeat},` +
            `'initialDelay':${song.initialDelay},` +
            `'difficultyTagging':${difficultyTagging}` +
        `}},`,"utf8");

    // Check whether this song already exists.
    const idMarker = Buffer.from(`'id':'${songId}'`, "ascii");

    if (data.indexOf(idMarker, insertPos) !== -1) {
        console.log(`Song already exists: ${songId}`);
        process.exit(0);
    }

    const output = Buffer.concat([
        data.subarray(0, insertPos),
        entry,
        data.subarray(insertPos)
    ]);

    fs.writeFileSync(file, output);

    console.log(`Added: ${songId}`);
    console.log(`Original size: ${data.length}`);
    console.log(`New size:      ${output.length}`);
}

else if (command === "remove") {

    const idMarker = Buffer.from(`'id':'${songId}'`, "ascii");
    const idPos = data.indexOf(idMarker, insertPos);

    if (idPos === -1) {
        console.log(`Song not found: ${songId}`);
        process.exit(0);
    }

    /*
        Find the opening { of the manifest entry.
        Then find its matching } while respecting strings.
    */

    let start = idPos;

    while (start > insertPos && data[start] !== 0x7b) { // {
        start--;
    }

    if (data[start] !== 0x7b) {
        throw new Error("Could not find song entry start.");
    }

    let depth = 0;
    let inString = false;
    let escaped = false;
    let end = -1;

    for (let i = start; i < data.length; i++) {

        const c = data[i];

        if (inString) {

            if (escaped) {
                escaped = false;
            }
            else if (c === 0x5c) { // \
                escaped = true;
            }
            else if (c === 0x27) { // '
                inString = false;
            }

            continue;
        }

        if (c === 0x27) { // '
            inString = true;
        }
        else if (c === 0x7b) { // {
            depth++;
        }
        else if (c === 0x7d) { // }
            depth--;

            if (depth === 0) {
                end = i + 1;
                break;
            }
        }
    }

    if (end === -1) {
        throw new Error("Could not find song entry end.");
    }

    // The entry has a comma after it.
    if (data[end] === 0x2c) { // ,
        end++;
    }

    const output = Buffer.concat([
        data.subarray(0, start),
        data.subarray(end)
    ]);

    fs.writeFileSync(file, output);

    console.log(`Removed: ${songId}`);
    console.log(`Original size: ${data.length}`);
    console.log(`New size:      ${output.length}`);
}

else {
    console.error(`Unknown command: ${command}`);
    process.exit(1);
}