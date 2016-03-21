var data = [{'state': 'Alabama', 'total': 60, 'pledged': 53},
{'state': 'Alaska', 'total': 20, 'pledged': 0},
{'state': 'Arizona', 'total': 85, 'pledged': 0},
{'state': 'Arkansas', 'total': 37, 'pledged': 32},
{'state': 'California', 'total': 548, 'pledged': 0},
{'state': 'Colorado', 'total': 78, 'pledged': 66},
{'state': 'Connecticut', 'total': 71 , 'pledged': 0},
{'state': 'Delaware', 'total': 31, 'pledged': 0},
{'state': 'District Of Columbia', 'total': 46, 'pledged': 0},
{'state': 'Florida', 'total': 246, 'pledged': 214},
{'state': 'Georgia', 'total': 117, 'pledged': 102},
{'state': 'Hawaii', 'total': 35, 'pledged': 0},
{'state': 'Idaho', 'total': 27, 'pledged': 0},
{'state': 'Illinois', 'total': 182, 'pledged': 156},
{'state': 'Indiana', 'total': 92, 'pledged': 0},
{'state': 'Iowa', 'total': 52, 'pledged': 44},
{'state': 'Kansas', 'total': 37, 'pledged': 33},
{'state': 'Kentucky', 'total': 60, 'pledged': 0},
{'state': 'Louisiana', 'total': 59, 'pledged': 51},
{'state': 'Maine', 'total': 30, 'pledged': 25},
{'state': 'Maryland', 'total': 118, 'pledged': 0},
{'state': 'Massachusetts', 'total': 116, 'pledged': 91},
{'state': 'Michigan', 'total': 147, 'pledged': 130},
{'state': 'Minnesota', 'total': 93, 'pledged': 77},
{'state': 'Mississippi', 'total': 41, 'pledged': 36},
{'state': 'Missouri', 'total': 84, 'pledged': 71},
{'state': 'Montana', 'total': 27, 'pledged': 0},
{'state': 'Nebraska', 'total': 30, 'pledged': 25},
{'state': 'Nevada', 'total': 43, 'pledged': 35},
{'state': 'New Hampshire', 'total': 32, 'pledged': 24},
{'state': 'New Jersey', 'total': 142, 'pledged': 0},
{'state': 'New Mexico', 'total': 43, 'pledged': 0},
{'state': 'New York', 'total': 291, 'pledged': 0},
{'state': 'North Carolina', 'total': 121, 'pledged': 107},
{'state': 'North Dakota', 'total': 23, 'pledged': 0},
{'state': 'Ohio', 'total': 160, 'pledged': 143},
{'state': 'Oklahoma', 'total': 42, 'pledged': 38},
{'state': 'Oregon', 'total': 74, 'pledged': 0},
{'state': 'Pennsylvania', 'total': 210, 'pledged': 0},
{'state': 'Rhode Island', 'total': 33, 'pledged': 0},
{'state': 'South Carolina', 'total': 59, 'pledged': 53},
{'state': 'South Dakota', 'total': 25, 'pledged': 0},
{'state': 'Tennessee', 'total': 75, 'pledged': 67},
{'state': 'Texas', 'total': 251, 'pledged': 222},
{'state': 'Utah', 'total': 37, 'pledged': 0},
{'state': 'Vermont', 'total': 26, 'pledged': 16},
{'state': 'Virginia', 'total': 109, 'pledged': 95},
{'state': 'Washington', 'total': 118, 'pledged': 0},
{'state': 'West Virginia', 'total': 37, 'pledged': 0},
{'state': 'Wisconsin', 'total': 96, 'pledged': 0},
{'state': 'Wyoming', 'total': 18, 'pledged': 0}];

var foo = d3.scale.linear()
.domain([0, 548])
.range([0,548*1.5]);

d3.select('.chart')
.selectAll("div")
.data(data)
.enter().append('div')
.style('background-color', function(d){
	if( d.pledged == 0 )
		return "DarkGrey";
	else
		return "steelblue";})
.text(function(d){
	if( d.pledged == 0 )
		return d.total;
	else
		return d.pledged;
});

d3.select('.labels')
.selectAll("div")
.data(data)
.enter().append('div')
.text(function(d){
	return d.state; });

d3.select('.chart')
.selectAll("div").transition()
.duration(1500)
.style('width', function(d){
	if( d.pledged == 0 )
		return foo(d.total) + 'px';
	else
		return foo(d.pledged) + 'px'; });