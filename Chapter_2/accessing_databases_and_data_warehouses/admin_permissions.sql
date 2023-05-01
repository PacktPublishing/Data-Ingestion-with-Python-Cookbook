-- Execute each command separated to avoid problems
create ROLE administration;

grant alter,create,delete,drop,index,insert,select,update,trigger,alter routine,create routine, execute, create temporary tables on `cookbook_data`.* to 'administration';

grant 'administration' to 'admin';

set default role 'administration' to 'admin';