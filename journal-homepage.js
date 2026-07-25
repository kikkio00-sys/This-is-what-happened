// Connect the new journal-style homepage controls to the existing archive application.
document.addEventListener("click",event=>{
  const control=event.target.closest(".journal-tab[data-room], .desk-card button[data-room]");
  if(!control)return;
  const roomName=control.dataset.room;
  if(typeof openRoom==="function"&&roomName){
    openRoom(roomName);
  }
});
