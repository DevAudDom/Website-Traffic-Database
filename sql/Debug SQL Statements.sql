-- Delete all rows from all tables
	-- Order matters due to foreign key constraints
	
	-- Delete from access tables first (they reference other tables)
	DELETE FROM hilton_access;
	DELETE FROM fourseasons_access;
	DELETE FROM marriott_access;
	DELETE FROM shangri_access;
	
	-- Delete from keyword tables
	DELETE FROM hilton_keyword;
	DELETE FROM fourseasons_keyword;
	DELETE FROM marriott_keyword;
	DELETE FROM shangri_keyword;
	
	-- Delete from backlink tables
	DELETE FROM hilton_backlink;
	DELETE FROM fourseasons_backlink;
	DELETE FROM marriott_backlink;
	DELETE FROM shangri_backlink;
	
	-- Delete from visitor tables last (they are referenced by access tables)
	DELETE FROM hilton_visitor;
	DELETE FROM fourseasons_visitor;
	DELETE FROM marriott_visitor;
	DELETE FROM shangri_visitor;
-- Find serial
-- SELECT pg_get_serial_sequence('marriott_backlink', 'backlink_id');
-- Reset serials 
	ALTER SEQUENCE public.fourseasons_backlink_backlink_id_seq RESTART WITH 1;
	ALTER SEQUENCE public.fourseasons_keyword_keyword_id_seq RESTART WITH 1;
	ALTER SEQUENCE public.marriott_backlink_backlink_id_seq RESTART WITH 1;
	ALTER SEQUENCE public.marriott_keyword_keyword_id_seq RESTART WITH 1;
	ALTER SEQUENCE public.hilton_backlink_backlink_id_seq RESTART WITH 1;
	ALTER SEQUENCE public.hilton_keyword_keyword_id_seq RESTART WITH 1;
	ALTER SEQUENCE public.shangri_backlink_backlink_id_seq RESTART WITH 1;
	ALTER SEQUENCE public.shangri_keyword_keyword_id_seq RESTART WITH 1;