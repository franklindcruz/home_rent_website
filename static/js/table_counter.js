//Create javascript file to count table fields

document.addEventListener("DOMContentLoaded", () => {
  const table = document.getElementById("customerTable");
  const rows = table.querySelectorAll("tbody tr");

  rows.forEach((row, index) => {
    const serialNumberCell = row.querySelector(".serial-number");
    serialNumberCell.textContent = index + 1;
  });
});
