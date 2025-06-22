function c_alert(msg,timeout=5.0)
{
    var overlay = $("<div></div>").css({
position:"fixed",
top:0,
left: 0,                  
width: "100%",     
height: "100%",    
backgroundColor: "rgba(0, 0, 0, 0.5)", 
zIndex: 99999        
});

// 2. Create the content div to center inside the overlay
var content = $("<div></div>").html("<h1 style='color:red;'>"+msg+"</h1><h2>Will Start in 5 Seconds...</h2>").css({
position: "relative", 
width:"50%", 
top: "50%",            
left: "50%",           
transform: "translate(-50%, -50%)", 
padding: "20px",
backgroundColor: "white",  
borderRadius: "8px",      
textAlign: "center"
});

// 3. Append the content div to the overlay
overlay.append(content);

// 4. Append the overlay to the body
$("body").append(overlay);

// Optional: To remove the overlay when clicked
setTimeout(function() {
overlay.remove();
},timeout*1000.0);
}
