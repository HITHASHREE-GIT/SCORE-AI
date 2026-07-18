import React from "react";
import DashboardCard from "../components/DashboardCard";
import SecurityChart from "../components/SecurityChart";


function Dashboard(){

return(

<div className="dashboard">

<h1>
SCORE Security Dashboard
</h1>


<div className="dashboard-grid">


<DashboardCard
title="Cloud Security Score"
value="92%"
/>


<DashboardCard
title="AWS Status"
value="Healthy"
/>


<DashboardCard
title="Azure Status"
value="Warning"
/>


<DashboardCard
title="Active Threats"
value="5"
/>


</div>

<SecurityChart />

<div className="alerts">

<h2>
Recent Security Alerts
</h2>


<table>

<thead>

<tr>
<th>Severity</th>
<th>Issue</th>
<th>Status</th>
</tr>

</thead>


<tbody>


<tr>
<td>High</td>
<td>Public S3 Bucket Exposure</td>
<td>Open</td>
</tr>


<tr>
<td>Medium</td>
<td>Unused IAM Permission</td>
<td>Review</td>
</tr>


<tr>
<td>Low</td>
<td>Open Network Port</td>
<td>Fixed</td>
</tr>


</tbody>

</table>


</div>


</div>

)

}


export default Dashboard;