$(document).ready(function () {
   $.getJSON('./sample.json', function (data) {
      if (data.length > 0) {
         var arrItems = [];              // The array to store JSON data.
         $.each(data, function (index, value) {
               arrItems.push(value);     // Push the value inside the array.
         });

         var _heading="", _timestamp="", _teams="", _spread="", _win="", _total="";
         var table = document.getElementById("next-events");
         var tstamp;
         var tr,td, headDiv,h2,dateTimeDiv, date, time, bets, aTag, team1Div, team2Div,team1Name,team2Name,team1Spread,team2Spread,team1Win,team2Win,team1Total,team2Total;
         for(var i=0; i<arrItems.length;i++){
            // tr = document.createElement('tr');
            // td = document.createElement('td');
            // headDiv = document.createElement('div');
            // headDiv.setAttribute('id','heading-div');
            // h2 = document.createElement('h2');
            _heading = arrItems[i].heading;
            console.log(_heading)
            // h2.innerHTML = _heading;
            for(var match in arrItems[i].matches){
               console.log(arrItems[i].matches)
               // console.log(arrItems[i].matches[match])
               _timestamp = arrItems[i].matches[match]
               _teams = arrItems[i].matches[match]
               _spread = arrItems[i].matches[match]
               _win = arrItems[i].matches[match]
               _total = arrItems[i].matches[match]
               // dateTimeDiv = document.createElement('div');
               // dateTimeDiv.setAttribute('id', 'date-time-div');
               // date = document.createElement('span')
               // date.setAttribute('id','date')
               // time = document.createElement('span')
               // time.setAttribute('id','time')
               // bets = document.createElement('span')
               // bets.setAttribute('id','bets')
               // if(_timestamp.length>0){
               //    date.innerHTML = tstamp;
               //    time.innerHTML = _timestamp[1]+" (Time)";
               // }
               // aTag = document.createElement('a');
               // team1Div = document.createElement('div')
               // team2Div = document.createElement('div')
               // team1Div.setAttribute('id','team1')
               // team2Div.setAttribute('id','team2')
               // team1Div.setAttribute('class','team')
               // team2Div.setAttribute('class','team')
               
               // // Team 1 creating elements
               // team1Name = document.createElement('span')
               // team1Spread = document.createElement('span')
               // team1Win = document.createElement('span')
               // team1Total = document.createElement('span')
               // team1Name.setAttribute('id','team1-name')
               // team1Spread.setAttribute('id','team1-spread')
               // team1Win.setAttribute('id','team1-win')
               // team1Total.setAttribute('id','team1-total')

               // // Team 2 creating elements
               // team2Name = document.createElement('span')
               // team2Spread = document.createElement('span')
               // team2Win = document.createElement('span')
               // team2Total = document.createElement('span')
               // team2Name.setAttribute('id','team2-name')
               // team2Spread.setAttribute('id','team2-spread')
               // team2Win.setAttribute('id','team2-win')
               // team2Total.setAttribute('id','team2-total')

               // if(_teams.length>0){
               //    team1Name.innerHTML = _teams[0];
               //    team2Name.innerHTML = _teams[1];
               //    bets.innerHTML = _teams[2]
               // }
               // if(_spread.length>0){
               //    team1Spread.innerHTML = _spread[0]+" - Spread";
               //    team2Spread.innerHTML = _spread[1]+" - Spread";
               // }
               // else{
               //    team1Spread.innerHTML = "None - Spread";
               //    team2Spread.innerHTML = "None - Spread"
               // }
               // if(_win.length>0){
               //    team1Win.innerHTML = _win[0]+" - Win";
               //    team2Win.innerHTML = _win[1]+" - Win";
               // }
               // if(_total.length>0){
               //    team1Total.innerHTML = _total[0]+" - Total";
               //    team2Total.innerHTML = _total[1]+" - Total";
               // }
               // else{
               //    team1Total.innerHTML = "None - Total";
               //    team2Total.innerHTML = "None - Total";
               // }

               // team1Div.appendChild(team1Name);
               // team1Div.appendChild(document.createElement('br'))
               // team1Div.appendChild(team1Spread);
               // team1Div.appendChild(document.createElement('br'))
               // team1Div.appendChild(team1Win);
               // team1Div.appendChild(document.createElement('br'))
               // team1Div.appendChild(team1Total);
               // team1Div.appendChild(document.createElement('br'))
               
               // team2Div.appendChild(team2Name);
               // team2Div.appendChild(document.createElement('br'))
               // team2Div.appendChild(team2Spread);
               // team2Div.appendChild(document.createElement('br'))
               // team2Div.appendChild(team2Win);
               // team2Div.appendChild(document.createElement('br'))
               // team2Div.appendChild(team2Total);
               // team2Div.appendChild(document.createElement('br'))
               
               // aTag.appendChild(team1Div);
               // aTag.appendChild(team2Div);

               // dateTimeDiv.appendChild(date)
               // dateTimeDiv.appendChild(time)
               // dateTimeDiv.appendChild(bets)
               
               // headDiv.appendChild(h2)
               // headDiv.appendChild(dateTimeDiv)
               // headDiv.appendChild(aTag)

               // td.appendChild(headDiv)
               
            }
         //    tr.appendChild(td)
         //    table.appendChild(tr)
          }
      }
   });
});