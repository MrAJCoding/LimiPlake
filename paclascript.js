document.getElementById("sunburstButton").addEventListener("click", function () {
    console.log("Button clicked!"); // Debug log
    const audio = new Audio("snbrst.mp3"); // Ensure correct path
    audio.play();
});
document.getElementById("riverButton").addEventListener("click", function () {
    console.log("Button clicked!"); // Debug log
    const audio = new Audio("rvrsng.mp3"); // Ensure correct path
    audio.play();
});
