// Toggles filter buttons

function toggle(btnName) {
    const button = document.querySelector(`#${btnName}`);
    const displayList = button.nextElementSibling;
    displayList.classList.toggle("closed");
}

