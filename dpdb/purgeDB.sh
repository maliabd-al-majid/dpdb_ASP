#!/usr/bin/env bash


# STOP ALL WORKING Sessions for logicsem DB



 psql -U postgres -c 'create or replace function pg_kill_all_sessions(db varchar, application varchar)
returns integer as
$$
begin
return (select count(*) from (select pg_catalog.pg_terminate_backend(pid) from pg_catalog.pg_stat_activity where pid <> pg_backend_pid() and datname = db and application_name = application) k);
end;
$$
language plpgsql security definer volatile set search_path = pg_catalog;

'

 psql -U postgres  -c 'select pg_kill_all_sessions('"'"'logicsem'"'"','"'"'dpdb'"'"');'



# Droping logicsem DB

 psql -U postgres -c 'DROP DATABASE  logicsem;'


#Creating logicsem DB

 psql -U postgres -c 'CREATE DATABASE logicsem;'


 psql -U postgres -c 'create or replace function pg_kill_all_sessions(db varchar, application varchar)
returns integer as
$$
begin
return (select count(*) from (select pg_catalog.pg_terminate_backend(pid) from pg_catalog.pg_stat_activity where pid <> pg_backend_pid() and datname = db and application_name = application) k);
end;
$$
language plpgsql security definer volatile set search_path = pg_catalog;

'



