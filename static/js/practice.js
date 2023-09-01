"use strict";

// Get references to DOM elements
const sidebarList = document.getElementById("sidebar-list");

const titlePlaceholder = document.getElementById("title-placeholder");
const detailsPlaceholder = document.getElementById("details-placeholder");

const previousButton = document.getElementById("previous-button");
const nextButton = document.getElementById("next-button");
const tryButton = document.getElementById("try-button");

// Set initial state
let currentItemIndex = 0;
let preItemIndex = 0;
let nextItemIndex = 0;


activate(currentItemIndex);

function activate(index) {
  // console.log(index);
  // Get the list item at the specified index
  const currentItem = sidebarList.getElementsByTagName("li")[index];

  // Clear the title placeholder
  titlePlaceholder.innerHTML = "";
  detailsPlaceholder.innerHTML = "";

  // activeItem.remove("active");
  let activeList = $("#sidebar-list").find("li.active");
  for (var i = 0; i < activeList.length; i++) {
    activeList[i].classList.remove("active");
  }

  currentItem.classList.add("active");
  tryButton.setAttribute("data_id", index + 1);


  // Show the title in the placeholder
  const title = currentItem.innerHTML;
  titlePlaceholder.innerHTML = title;
  // console.log('Data ID', currentItem.getAttribute("data_id"));
  $.ajax({
    url: "/practice/" + currentItem.getAttribute("data_id"),
    
    success: function (response) {
      var question = response.result;
      // console.log( response);
      detailsPlaceholder.innerHTML = question.description;
    },
    
  });

  // Disable/enable buttons based on the current index
  previousButton.disabled = index === 0;
  nextButton.disabled = index === sidebarList.children.length - 1;

  $("li.active").animate({ scrollTop: 0 }, "slow");
}
// showtitle(preItemIndex, currentItemIndex, nextItemIndex);
$("#sidebar-list").on("click", (e) => {
  currentItemIndex = e.target.getAttribute("data_id");
  currentItemIndex--;
  // console.log(currentItemIndex);
  activate(currentItemIndex);
});

// Event listener for previous button
previousButton.addEventListener("click", () => {
  if (currentItemIndex > 0) {
    let activeList = $("#sidebar-list").find("li.active");
    preItemIndex = activeList[0].getAttribute("data_id");
    currentItemIndex = preItemIndex-2;
  }else{
    currentItemIndex--;
  }
  // console.log(currentItemIndex);
  activate(currentItemIndex);
});

// Event listener for next button
nextButton.addEventListener("click", () => {
  let activeList = $("#sidebar-list").find("li.active");
  nextItemIndex = activeList[0].getAttribute("data_id");
  currentItemIndex++;
  activate(currentItemIndex);
});

// Event listener for next button
tryButton.addEventListener("click", () => {
  window.open("/try/" + tryButton.getAttribute("data_id"));
});

// $(document).ready(function () {
//   var $scroll = $(".scrollspy-example");
//   $(this).scrollTop($("li.active").position().top);
// });