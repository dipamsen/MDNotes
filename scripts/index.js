// Generate PDF and HTML
const util = require("util");
const child_process = require("child_process");
const path = require("path");
const { readFileSync } = require("fs");
let TESTRUN = false;

const pdfOpts = [
  "--metadata-file",
  "config/pdf-meta.yaml",
  "--resource-path=..",
  "-s",
  "--shift-heading-level-by",
  "-1",
  "--template",
  "templates/default.latex",
  "--lua-filter",
  "filters/imgresolve.lua",
  "-V",
  "headertext=JEE Mathematics (11)",
];

(async () => {
  const args = process.argv.slice(2);
  // console.log(args);
  const inputFile = args[0];
  if (args[1] && args[1] === "-t") {
    TESTRUN = true;
  }

  // Input File: src/Mathematics/Sets.md
  // Output File: out/Mathematics/Sets.pdf

  // get folder name and file name of input file
  const file = path.parse(inputFile).name;
  const folder = path
    .parse(inputFile)
    .dir.split("\\")
    .filter((x) => x)
    .pop();

  console.log("PROGRAM: Converting", folder, "-", file);

  const pdfOut = path.join("out", folder, "pdf", file + ".pdf");
  const htmlOut = path.join("out", folder, "html", file + ".html");

  // Convert to HTML
  await createHTML(inputFile, htmlOut);
  console.log(htmlOut);

  console.log("");
  // Convert to PDF
  await createPDF(inputFile, pdfOut);
  console.log(pdfOut);

  console.log("");
  if (TESTRUN) {
    console.log("");
    const latexOut = path.join("test", folder + "-" + file + ".tex");
    await createLaTeX(inputFile, latexOut);
    console.log(latexOut);
  }
})();

function createHTML(input, output) {
  return new Promise((res, rej) => {
    // const [, title] = readFileSync(input)
    //   .toString()
    //   .match(/# (.*)[\*]/);
    run_script(
      "pandoc",
      [
        "-o",
        output,
        input,
        "--metadata-file",
        "config/html-meta.yaml",
        "--katex",
        "-s",
        "-V",
        // "pagetitle=" + title.replace(/\*/g, "") + "",
        "--template",
        "templates/default.html",
      ],
      (code) => {
        if (code === 0) {
          console.log("HTML Created.");
          res();
        }
        if (code !== 0) {
          console.error("HTML Failed.");
          rej();
        }
      },
      "HTML"
    );
  });
}

function createPDF(input, output) {
  return new Promise((res, rej) => {
    run_script(
      "pandoc",
      ["-o", output, input, ...pdfOpts],
      (code) => {
        if (code === 0) {
          console.log("PDF Created.");
          res();
        }
        if (code !== 0) {
          console.error("PDF Failed.");
          rej();
        }
      },
      "PDF"
    );
  });
}

function createLaTeX(input, output) {
  return new Promise((res, rej) => {
    run_script(
      "pandoc",
      ["-o", output, input, ...pdfOpts],
      (code) => {
        if (code === 0) {
          console.log("LaTeX Created.");
          res();
        }
        if (code !== 0) {
          console.error("LaTeX Failed.");
          rej();
        }
      },
      "LaTeX"
    );
  });
}

// https://stackoverflow.com/questions/14332721/node-js-spawn-child-process-and-get-terminal-output-live
// This function will output the lines from the script
// AS is runs, AND will return the full combined output
// as well as exit code when it's done (using the callback).
function run_script(command, args, callback, cmdCode) {
  console.log("Starting Process.");
  var child = child_process.spawn(command, args);

  child.stdout.setEncoding("utf8");
  child.stdout.on("data", function (data) {
    console.log(`[${cmdCode}]: ` + data);
  });

  child.stderr.setEncoding("utf8");
  child.stderr.on("data", function (data) {
    console.error(data);
  });

  child.on("close", function (code) {
    callback(code);
  });
}
