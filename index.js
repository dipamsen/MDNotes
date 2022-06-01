// Generate PDF and HTML
const util = require("util");
const exec = util.promisify(require("child_process").exec);

(async () => {
  const { stdout, stderr } = await exec("echo HELLO PEOPLE");
  console.log(stdout);
  console.error(stderr);

  const mdFile = process.argv[process.argv.length - 1];
  const filename = mdFile.split(".")[0];
  const htmlCmd = `pandoc -o ${filename}.html ${filename}.md --metadata-file html-meta.yaml --katex -s`;
  const pdfCmd = `pandoc -o ${filename}.pdf ${filename}.md --metadata-file pdf-meta.yaml -s --shift-heading-level-by -1 --template templates/default.latex --from markdown+raw_html`;
  // const texCmd = `pandoc -o ${filename}.tex ${filename}.md --metadata-file pdf-meta.yaml -s --shift-heading-level-by -1 --template templates/default.latex`;

  console.log("Converting to HTML. (Using KaTeX)");
  const htmlP = await exec(htmlCmd);
  console.log(htmlP.stdout);
  console.error(htmlP.stderr);
  console.log("Done with HTML.");

  console.log("");

  console.log("Converting to PDF. (Using PDFLaTeX)");
  const pdfP = await exec(pdfCmd);
  console.log(pdfP.stdout);
  console.error(pdfP.stderr);
  console.log("Done with PDF.");

  console.log("");

  // console.log("Converting to TeX. (Using PDFLaTeX)");
  // const texP = await exec(texCmd);
  // console.log(texP.stdout);
  // console.error(texP.stderr);
  // console.log("Done with TeX.");
})();
