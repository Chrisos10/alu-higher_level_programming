-- a script that creates the MYSQL server user user_od_1
-- user_od_1 should have all privileges on MYSQL server
-- THe user_od_1 shuld have password user_od_1_pwd
-- if user_od_1nexists, the script should not fail
CREATE USER IF NOT ÈXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
REVOKE AUDIT_ABORT_EXEMPT, FIREWALL_EXEMPT, AUTHENTICATION_POLICY_ADMIN, GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN, SENSITIVE_VARIABLES_OBSERVER, TELEMETRY_LOG_ADMIN ON *.* FROM 'user_0d_1'@'localhost';
