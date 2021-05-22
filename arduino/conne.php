<?php


$dbServername = "localhost";
$dbUsername = "root";
$dbPassword = "";
$dbName = "eshop";

$conn = mysqli_connect($dbServername, $dbUsername ,$dbPassword , $dbName);


if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";

?>



<center>
		<h1> Eshop </h1>

		<form  method="POST">
				<input type="text" name="id" placeholder="Enter 1 2 or 3"/><br/>
				
				<input type="submit" name="update" value="Agora"/>

			</form>
			
</body>
</html>


<?php 

$db = mysqli_select_db($conn,'eshop');

if(isset($_POST['update']))
{ 
	
	$id = '$_GET[id]';
	$query = "UPDATE proionta SET apothema=apothema-1 WHERE id='$_POST[id]'";
	$query_run = mysqli_query($conn,$query);

	if($query_run){
		echo "Οκ";
	
}	
}
?>