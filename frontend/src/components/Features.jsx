import React from "react";
import FeatureCard from "./FeatureCard";

function Features(){

const features=[
{
title:"Cloud Security Scan",
description:"Scan AWS and Azure resources for security issues."
},
{
title:"AI Alert Prioritization",
description:"Reduce unnecessary alerts using machine learning."
},
{
title:"Real Time Monitoring",
description:"Monitor cloud activities instantly."
}
];


return(

<section id="features">

<h2>
Features
</h2>

<div className="features-container">

{
features.map((item,index)=>(

<FeatureCard
key={index}
title={item.title}
description={item.description}
/>

))
}

</div>

</section>

)

}

export default Features;