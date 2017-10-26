#!"C:\Perl64\bin\perl.exe"
use strict;
use warnings;
use CGI;
use DBI;
use JSON;
my @output;
my $cgi = CGI->new;
#accept data as parameter
my $matchValue = $cgi->param('data_search'); 
my $driver = "mysql"; 
my $database = "appointmentPerldb";
my $dsn = "DBI:$driver:database=$database";
my $userid = "root";
my $password = "root";
my $dbh = DBI->connect($dsn, $userid, $password ) or die $DBI::errstr;
#SQL query to find search all the records from the database which matches string(id)
my $sqlc = "SELECT appointment_date, appointment_time, description FROM appointmentMaster where description like '%".$matchValue."%'"; 
my $sth = $dbh->prepare($sqlc);
$sth->execute;
while ( my $row = $sth->fetchrow_hashref ){
    push @output, $row;
}
my $cgi = CGI->new;
print $cgi->header( 'application/json' );
#print objToJson( { myData => \@output } );
print objToJson(  \@output  );