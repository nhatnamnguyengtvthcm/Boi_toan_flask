$( document ).ready(function(){
    $("#nguhanh").click(function(){
        // var flag = 0;
        // var result={};
        var a =document.getElementById("nguhanh");
        var man = document.getElementById("nam").value;
        var woman = document.getElementById("nu").value;
    
        var man_year = parseInt(man);
        var woman_year = parseInt(woman);
            
        var year_of_birth = JSON.stringify({
            fun: 0,
            man_year: man_year,
            woman_year : woman_year
        }) ;
        
        $.ajax({

            type:"POST",
            url: "http://127.0.0.1:5000/boitoan/",
            data: year_of_birth,
            dataType: "json",
            contentType: "application/json;charset=UTF-8",
            success: function(response){
                console.log(response);
                result = response;
                alert("Canh chi của nam: " + result["man_can_chi"]+ "\r" +
                      "Cệnh của nam: " + result["man_menh"]+ "\r" + 
                      "Canh chi của nữ: " + result["woman_can_chi"]+ "\r" +
                      "Mệnh của nữ: " + result["woman_menh"]+ "\r")
                    }
        });    
    });
    
    $("#hoptuoi").click(function(){
        var a =document.getElementById("nguhanh");
        var man = document.getElementById("nam").value;
        var woman = document.getElementById("nu").value;
    
        var man_year = parseInt(man);
        var woman_year = parseInt(woman);
            
        var year_of_birth = JSON.stringify({
            fun: 1,
            man_year: man_year,
            woman_year : woman_year
        }) ;
        
        $.ajax({

            type:"POST",
            url: "http://127.0.0.1:5000/boitoan/",
            data: year_of_birth,
            dataType: "json",
            contentType: "application/json;charset=UTF-8",
            success: function(response){
                console.log(response);
                result = response;
                if (result["ket_qua"] == "Cát")
                {
                    alert("Cung của bạn nam: "+result["cung_nam"]+"\r"+
                      "Cung của bạn nữ: " +result["cung_nu"]+"\r"+
                      "Cung kết hợp: " +result["cung_ket_hop"]+"\r"+
                      "Kết quả: " +result["ket_qua"]+ "(Hợp tuổi)" +"\r"
                    ) 

                }
                else
                {
                    alert("Cung của bạn nam: "+result["cung_nam"]+"\r"+
                      "Cung của bạn nữ: " +result["cung_nu"]+"\r"+
                      "Cung kết hợp: " +result["cung_ket_hop"]+"\r"+
                      "Kết quả: " +result["ket_qua"]+ "(Không hợp tuổi)" +"\r"
                    ) 
                }
                
            }
        });    
    });
});