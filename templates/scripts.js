
<script>
    var acc = document.getElementsByClassName("accordion");
    var i;
    
    for (i = 0; i < acc.length; i++) {
      acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.display === "form") {
          panel.style.display = "form";
        } else {
          panel.style.display = "form";
        }
      });
    }



      function ddlselect()
         {
             var d=document.getElementById("product");
             var displaytext=d.options[d.selectedIndex].text;
             document.getElementById("lpattitype").value=venila;
                   
          }


    </script>