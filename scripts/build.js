const child_process = require("child_process");
const path = require("path");
const fs = require("fs").promises;

(async () => {
  const dirs = (await fs.readdir("src")).map((fol) => `src\\${fol}`);
  console.log(dirs);
  for (const folder of dirs) {
    const files = await fs.readdir(folder);
    const chaps = new Set(files.map((x) => path.parse(x).name));
    for (const chap of chaps) {
      console.log("==================================");
      console.log("Converting " + chap);
      console.log("==================================");
      await run_script(`node`, ["scripts/index.js", `${folder}\\${chap}.md`]);
    }
  }
})();

function run_script(command, args) {
  return new Promise((resolve, reject) => {
    var child = child_process.spawn(command, args);

    child.stdout.setEncoding("utf8");
    child.stdout.on("data", function (data) {
      console.log(data);
    });

    child.stderr.setEncoding("utf8");
    child.stderr.on("data", function (data) {
      console.error(data);
    });

    child.on("close", function (code) {
      if (code == 0) resolve(code);
      else reject(code);
    });
  });
}
