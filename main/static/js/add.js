const addBtn1 = document.querySelector('.add_button_partners');
const form1 = document.querySelector('.partners_item');
addBtn1.onclick = () => {
  form1.after(form1.cloneNode(true));
}

const addBtn2 = document.querySelector('.add_button_teams');
const form2 = document.querySelector('.teams_item');
addBtn2.onclick = () => {
  form2.after(form2.cloneNode(true));
}

const addBtn3 = document.querySelector('.add_button_events');
const form3 = document.querySelector('.events_item');
addBtn3.onclick = () => {
  form3.after(form3.cloneNode(true));
}