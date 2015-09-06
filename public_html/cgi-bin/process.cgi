#! /bin/bash

# This is a little CGI program
###################################################################
# The following are environment variables that are available to you
#
# CONTENT_TYPE:      The desired MIME type for the response.
# CONTENT_LENGTH:    The length of the query information.
# GATEWAT_INTERFACE: Currently CGI/1.1
# HTTP_HOST:         The name of the vhost of the server.
# HTTP_USER_AGENT:   Information about the requesting client.
# QUERY_STRING:      The query string.
# REQUEST_METHOD:    The method used to make the request. 
# REQUEST_URI:       The URI of the request.
# SERVER_PROTOCOL:   Currently “HTTP/1.1”.
# SCRIPT_FILENAME:   The full path to the CGI script.
# SCRIPT_NAME:       The name (i.e., URI) of the CGI script.
# SERVER_NAME:       The server's hostname or IP Address.
# SERVER_PORT:       The port of the server.

# Add a content type and a blank line

echo "X-COMP-490: Hi there I am Michael"
echo "Content-type: text/html"
echo ""
echo "<html>"
echo "<HEAD>"
echo "<link rel="stylesheet" type="text/css" href="../css/style.css">"
echo "<TITLE>Comp490-Project 1 </TITLE></HEAD>"
echo "<body>"
echo "<p> This first projcet which is getting name and eamil address from user</p>"
echo 
if [ "$QUERY_STRING" ] ; then
  echo " <p> ./$QUERY_STRING</p>"
fi
echo "</body>"
echo "</html>"
