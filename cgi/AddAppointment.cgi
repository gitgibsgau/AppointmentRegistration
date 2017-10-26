#!"C:\Perl64\bin\perl.exe"
use warnings;
use CGI;
use DBI;
print "Content-Type: text/html\n\n";
#Getting values from the CGI Environment variable.
my $q = CGI::Vars();
my $appointment_date = $q->{Date};
my $appointment_time = $q->{Time};
my $description = $q->{Description};
#remove trailing spaces u
$appointment_date =~ s/^\s*(.*?)\s*$/$1/;
$appointment_time =~ s/^\s*(.*?)\s*$/$1/;
$description =~ s/^\s*(.*?)\s*$/$1/;
#Database operation using perl
my $driver = "mysql"; 
my $database = "appointmentPerldb";
my $dsn = "DBI:$driver:database=$database";
my $userid = "root";
my $password = "root";
#Connection to the database
my $dbh = DBI->connect($dsn, $userid, $password ) or die $DBI::errstr;
#Insert records to the database;
my $sth = $dbh->prepare("INSERT INTO appointmentMaster
                       (appointment_date, appointment_time, description)
                        values
                       ('$appointment_date', '$appointment_time', '$description')");
$sth->execute() or die $DBI::errstr;
$sth->finish();
# redirect to home page
print "<META HTTP-EQUIV=refresh CONTENT=\"1;URL=../home.html\">\n";

