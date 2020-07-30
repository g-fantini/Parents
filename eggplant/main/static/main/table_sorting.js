/**
 * Summary. Returns the value associated to the given GET parameter
   @param {str} parameter  get parameter required
   @return {str} Return the value of the given parameter
 */
function getParameter(parameter)
{
	var queryString = window.location.search;
	var urlParams = new URLSearchParams(queryString);
	return urlParams.get(parameter);
}


function updateSortingMethod()
{
	//get sorting method and field
	var method = getParameter("sort");
	if(method)
	{
		var order ="";
		//Check if the sorting order is ASC or DESC
		(method.includes("-")) ? order="(DESC)" : order="(ASC)";
	
		document.getElementById("sortingmethod").innerHTML = method.replace("-", "") +" "+ order;
	}
}

//Create listener on the DOMContentLoaded to update the sorting method paragraph 
document.addEventListener("DOMContentLoaded", updateSortingMethod);
