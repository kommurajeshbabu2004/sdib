async function testAPI() {

    const response = await fetch('http://localhost:8080/products');
    const data = await response.json();

    console.log(data);
}

testAPI();
