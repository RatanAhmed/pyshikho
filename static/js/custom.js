// Get references to DOM elements
const sidebarList = document.getElementById('sidebar-list');
const contentPlaceholder = document.getElementById('content-placeholder');
const detailsPlaceholder = document.getElementById('details-placeholder');
const previousButton = document.getElementById('previous-button');
const nextButton = document.getElementById('next-button');
const tryButton = document.getElementById('try-button');

// Set initial state
let currentItemIndex = 0;
let preItemIndex = 0;
showContent(currentItemIndex);

// Function to show content based on index
function showContent(index, pre) {
  // Get the list item at the specified index
  const listItem = sidebarList.getElementsByTagName('li')[index];
  const preItem = sidebarList.getElementsByTagName('li')[pre];
   
  // Clear the content placeholder
  contentPlaceholder.innerHTML = '';
  detailsPlaceholder.innerHTML = '';
  
  if(preItem){
    preItem.classList.remove("active");
  }
  listItem.classList.add("active");
  tryButton.setAttribute("data_id",index+1);

  // Show the content in the placeholder
  const content = listItem.innerHTML;
  contentPlaceholder.innerHTML = content;
  
  $.ajax({
    url: '/question/'+listItem.getAttribute('data_id'),

    success: function (response) {
        var question = response.result;
        detailsPlaceholder.innerHTML = question.description;
    }
  });
  
  // Disable/enable buttons based on the current index
  previousButton.disabled = index === 0;
  nextButton.disabled = index === sidebarList.children.length - 1;
}

// Event listener for previous button
previousButton.addEventListener('click', () => {
  if (currentItemIndex > 0) {
    preItemIndex = currentItemIndex
    currentItemIndex--;
    showContent(currentItemIndex,preItemIndex);
  }
});

// Event listener for next button
nextButton.addEventListener('click', () => {
  if (currentItemIndex < sidebarList.children.length - 1) {
    preItemIndex = currentItemIndex
    currentItemIndex++;
    
    showContent(currentItemIndex, preItemIndex);
  }
});

// Event listener for next button
tryButton.addEventListener('click', () => {
    window.open('/try/'+tryButton.getAttribute('data_id'))
});

