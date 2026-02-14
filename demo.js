employees=[
    {empid:1,empname:"kommu",empsalary:10000},
    {empid:2,empname:"sai",empsalary:20000},
    {empid:3,empname:"sai",empsalary:30000},
    {empid:4,empname:"sai",empsalary:40000},
    {empid:5,empname:"sai",empsalary:50000},
];
document.writeln("<table border='1'>");
document.writeln("<tr><th>Empid</th> <th>Empname</th> <th>Empsalary</th> </tr>");
for(let emp of employees){
    console.log(emp.empid+" \t "+emp.empname+" \t "+emp.empsalary);
    document.writeln("<tr><td>"+emp.empid+"</td> <td>"+emp.empname+"</td> <td>"+emp.empsalary+"</td> </tr>");
}