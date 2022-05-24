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
  const pdfCmd = `pandoc -o ${filename}.pdf ${filename}.md --metadata-file html-meta.yaml --katex -t html --variable header-html=Hi`;
//  --metadata-file html-meta.yaml -s -t html --katex
  console.log("Converting to HTML. (Using KaTeX)");
  const htmlP = await exec(htmlCmd);
  console.log(htmlP.stdout);
  console.error(htmlP.stderr);
  console.log("Done with HTML.");

  console.log("");

  console.log("Converting to PDF. (Using HTML2PDF)");
  const pdfP = await exec(pdfCmd);
  console.log(pdfP.stdout);
  console.error(pdfP.stderr);
  console.log("Done with PDF.");
})();
