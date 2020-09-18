create sequence warranty_id_seq
	as integer;

create table warranty
(
	id serial not null
		constraint warranty_pkey
			primary key,
	url varchar(200),
	name varchar(200),
	created_at timestamp default now(),
	last_updated timestamp,
	login_information json
);

create function update_modified_column() returns trigger
	language plpgsql
as $$
BEGIN
NEW.last_updated = now();
RETURN NEW;
END;
$$;

create trigger update_warranty_modtime
	before update
	on warranty
	for each row
	execute procedure update_modified_column();


create table if not exists log_system
(
	id serial not null
		constraint log_system_pkey
			primary key,
	document_number varchar(200) not null,
	operation_id uuid,
	warranty_id bigint
		constraint fk_warranty_name
			references warranty,
	message varchar(100),
	extra_information json,
	created_at timestamp default now(),
	last_updated timestamp
);




alter table warranty owner to test;

grant select, update, usage on sequence warranty_id_seq to public;

grant select, update, usage on sequence warranty_id_seq to public;

grant insert, select, update, references, trigger on warranty to public;

grant insert, select, update, references, trigger on warranty to public;

alter function update_modified_column() owner to test;

alter sequence warranty_id_seq owner to test;

grant select, update, usage on sequence warranty_id_seq to public;

grant select, update, usage on sequence warranty_id_seq to public;



insert into public.warranty (id, url, name, created_at, last_updated, login_information) values (1, 'https://rede-mobile.staging.captalysplatform.io/get-flow', 'rede', '2020-06-14 14:51:46.509680', null, null);
insert into public.warranty (id, url, name, created_at, last_updated, login_information) values (2, 'https://stone-mobile.staging.captalysplatform.io/get-flow', 'stone', '2020-06-14 17:47:14.252168', null, null);
insert into public.warranty (id, url, name, created_at, last_updated, login_information) values (3, 'https://getnet-mobile.staging.captalysplatform.io/get-flow', 'getnet', '2020-06-14 17:47:14.263667', null, null);
insert into public.warranty (id, url, name, created_at, last_updated, login_information) values (4, 'https://getnet-desktop.staging.captalysplatform.io/get-flow', 'getnet', '2020-06-14 17:47:14.274167', null, null);
insert into public.warranty (id, url, name, created_at, last_updated, login_information) values (5, 'https://bin-mobile.staging.captalysplatform.io/get-flow', 'bin', '2020-06-14 17:47:14.446048', null, null);
insert into public.warranty (id, url, name, created_at, last_updated, login_information) values (6, 'https://bin-desktop.staging.captalysplatform.io/get-flow', 'bin', '2020-06-14 17:47:14.456418', null, null);
insert into public.warranty (id, url, name, created_at, last_updated, login_information) values (7, 'https://cielo-desktop.staging.captalysplatform.io/get-flow', 'cielo', '2020-06-14 17:47:14.467277', null, null);