<?php

require('routeros_api.class.pho');

$API = new RouterosAPI();
$API->debug = true;

if($API->connect('192.168.26.244','admin','')){
    $API->write('/interface/getall');
    $READ = $API->read(false);
    $ARRAY = $API->parseResponse($READ);
    print_r($ARRAY);
    $API->disconnect();
}

?>