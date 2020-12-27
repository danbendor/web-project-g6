
       
          window.onload = function () {
                  
            var chart = new CanvasJS.Chart("chartContainer", {
                animationEnabled: true,
                exportEnabled: true,
                theme: "light2",
                title:{
                    text: "Sales amount"
                },
                 
           
                data: [{
                    type: "column", 
                    dataPoints: [
                        { x: 1, y: 100 },
                        { x: 2, y: 454 },
                        { x: 3, y: 32 },
                        { x: 4, y: 650 },
                        { x: 5, y: 92 },
                        { x: 6, y: 68 },
                        { x: 7, y: 380 },
                        { x: 8, y: 564 },
                        { x: 9, y: 44 },
                        { x: 10, y: 110 },
                        { x: 11, y: 233 },
                        { x: 12, y: 130 },
                 ]
                }]
            });
            chart.render();
            
            }


       
        
      