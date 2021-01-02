$(document).ready(function () {
   $.getJSON('./sample.json', function (data) {
      if (data.length > 0) {
         var arrItems = [];              // The array to store JSON data.
         $.each(data, function (index, value) {
               arrItems.push(value);     // Push the value inside the array.
         });

         var _heading="", _timestamp="", _teams="", _spread="", _win="", _total="";
         var table = document.getElementById("next-events");
         var tbody = document.createElement('tbody');
         var headtr,headtd,tr,td, headDiv,h2,dateTimeDiv, date, time, bets, aTag, team1Div, team2Div,team1Name,team2Name,team1Spread,team2Spread,team1Win,team2Win,team1Total,team2Total;
         for(var i=0; i<arrItems.length;i++){
            headtr = document.createElement('tr')
            headtd = document.createElement('td')
            tr = document.createElement('tr');
            td = document.createElement('td');
            
            h2 = document.createElement('h2');
            _heading = arrItems[i].header;
            console.log(_heading)
            h2.innerHTML = _heading;
            headtd.appendChild(h2);
            headtr.appendChild(headtd);
            tbody.appendChild(headtr);
            for(var match in arrItems[i].matches){
               _timestamp = arrItems[i].matches[match].timestamp.split("\n")
               _teams = arrItems[i].matches[match].teams.split("\n")
               _spread = arrItems[i].matches[match].spread.split("\n")
               _win = arrItems[i].matches[match].win.split("\n")
               _total = arrItems[i].matches[match].total.split("\n")
               // console.log("Timestamp: "+_timestamp+"\nTeams: "+_teams+"\nSpread: "+_spread+"\nWin: "+_win+"\nTotal: "+_total)

               console.log(_teams)

               dateTimeDiv = document.createElement('div');
               dateTimeDiv.setAttribute('id', 'date-time-div');
               date = document.createElement('span')
               date.setAttribute('id','date')
               time = document.createElement('span')
               time.setAttribute('id','time')
               bets = document.createElement('span')
               bets.setAttribute('id','bets')
               if(_timestamp.length>0){
                  date.innerHTML = _timestamp[0]+" (Date)";
                  time.innerHTML = _timestamp[1]+" (Time)";
               }

               headDiv = document.createElement('div');
               headDiv.setAttribute('id','heading-div');

               aTag = document.createElement('a');
               team1Div = document.createElement('div')
               team2Div = document.createElement('div')
               team1Div.setAttribute('id','team1')
               team2Div.setAttribute('id','team2')
               team1Div.setAttribute('class','team')
               team2Div.setAttribute('class','team')
               
               // Team 1 creating elements
               team1Name = document.createElement('span')
               team1Spread = document.createElement('span')
               team1Win = document.createElement('span')
               team1Total = document.createElement('span')
               team1Name.setAttribute('id','team1-name')
               team1Spread.setAttribute('id','team1-spread')
               team1Win.setAttribute('id','team1-win')
               team1Total.setAttribute('id','team1-total')

               // Team 2 creating elements
               team2Name = document.createElement('span')
               team2Spread = document.createElement('span')
               team2Win = document.createElement('span')
               team2Total = document.createElement('span')
               team2Name.setAttribute('id','team2-name')
               team2Spread.setAttribute('id','team2-spread')
               team2Win.setAttribute('id','team2-win')
               team2Total.setAttribute('id','team2-total')

               if(typeof(_teams) === 'undefined' || _teams == null || _teams == ""){
                  team1Name.innerHTML = "Not Specified";
                  team2Name.innerHTML = "Not Specified";
                  bets.innerHTML = "+0 Bets";
               }else{
                  team1Name.innerHTML = _teams[0];
                  team2Name.innerHTML = _teams[1];
                  bets.innerHTML = _teams[2]
               }
               if(typeof(_spread) === 'undefined' || _spread == null || _spread == ""){
                  team1Spread.innerHTML = "None - Spread";
                  team2Spread.innerHTML = "None - Spread";
               }else{
                  team1Spread.innerHTML = _spread[0]+" - Spread";
                  team2Spread.innerHTML = _spread[1]+" - Spread";
               }
               if(typeof(_win) === 'undefined' || _win == null || _win == ""){
                  team1Win.innerHTML = "∞ - Win";
                  team2Win.innerHTML = "∞ - Win";
               }else{
                  team1Win.innerHTML = _win[0]+" - Win";
                  team2Win.innerHTML = _win[1]+" - Win";
               }
               if(typeof(_total) === 'undefined' || _total == null || _total == ""){
                  team1Total.innerHTML = "None - Total";
                  team2Total.innerHTML = "None - Total";
               }else{
                  team1Total.innerHTML = _total[0]+" - Total";
                  team2Total.innerHTML = _total[1]+" - Total";
               }

               team1Div.appendChild(team1Name);
               team1Div.appendChild(document.createElement('br'))
               team1Div.appendChild(team1Spread);
               team1Div.appendChild(document.createElement('br'))
               team1Div.appendChild(team1Win);
               team1Div.appendChild(document.createElement('br'))
               team1Div.appendChild(team1Total);
               team1Div.appendChild(document.createElement('br'))
               
               team2Div.appendChild(team2Name);
               team2Div.appendChild(document.createElement('br'))
               team2Div.appendChild(team2Spread);
               team2Div.appendChild(document.createElement('br'))
               team2Div.appendChild(team2Win);
               team2Div.appendChild(document.createElement('br'))
               team2Div.appendChild(team2Total);
               team2Div.appendChild(document.createElement('br'))
               
               aTag.appendChild(team1Div);
               aTag.appendChild(team2Div);
               aTag.setAttribute("href","https://record.revenuenetwork.com/_gK7De1rYvgo2XUl_PBb-mGNd7ZgqdRLk/1/")

               dateTimeDiv.appendChild(date)
               dateTimeDiv.appendChild(time)
               dateTimeDiv.appendChild(bets)
               
               headDiv.appendChild(dateTimeDiv)
               headDiv.appendChild(aTag)

               td.appendChild(headDiv)
               
            }
            tr.appendChild(td)
            tbody.appendChild(tr)
         }
         table.appendChild(tbody);
      }
   });
});