import React from "react";

import {
  Line
} from "react-chartjs-2";


import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from "chart.js";


ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);



function SecurityChart(){


const data = {

labels:[
"Jan",
"Feb",
"Mar",
"Apr",
"May"
],


datasets:[

{

label:"Security Score",

data:[
70,
78,
85,
90,
92
],


borderWidth:3

}

]

};



return(

<div className="chart-box">


<h2>
Security Score Trend
</h2>


<Line data={data}/>


</div>

);


}


export default SecurityChart;