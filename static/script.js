document.getElementById("uploadForm").onsubmit = async function(e) {
  e.preventDefault();
  const formData = new FormData(this);
  await fetch("/upload", {
    method: "POST",
    body: formData
  });
  drawGraph();
};

async function drawGraph() {
  const res = await fetch("/graph");
  const data = await res.json();

  const container = document.getElementById("network");
  const options = {};
  const network = new vis.Network(container, data, options);
}

drawGraph();

async function runAlgo(type) {
  const start = document.getElementById("startNode").value;
  const res = await fetch(`/${type}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ start })
  });

  const data = await res.json();
  document.getElementById("output").innerText = `${type.toUpperCase()} Result: ${data.join(', ')}`;
}