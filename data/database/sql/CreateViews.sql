\set ON_ERROR_STOP 1

BEGIN;

CREATE OR REPLACE VIEW release_event AS
    SELECT
        release, date_year, date_month, date_day, country
    FROM (
        SELECT release, date_year, date_month, date_day, country
        FROM release_country
        UNION ALL
        SELECT release, date_year, date_month, date_day, NULL
        FROM release_unknown_country
    ) as q;

CREATE OR REPLACE VIEW artist_series AS
    SELECT entity0 AS artist,
           entity1 AS series,
           las.id AS relationship,
           link_order,
           las.link,
           COALESCE(text_value, '') AS text_value
    FROM l_artist_series las
    JOIN series s ON s.id = las.entity1
    JOIN link l ON l.id = las.link
    JOIN link_type lt ON (lt.id = l.link_type AND lt.gid = 'd1a845d1-8c03-3191-9454-e4e8d37fa5e0')
    LEFT OUTER JOIN link_attribute_text_value latv ON (latv.attribute_type = 788 AND latv.link = l.id)
    ORDER BY series, link_order;

CREATE OR REPLACE VIEW event_series AS
    SELECT entity0 AS event,
           entity1 AS series,
           lrs.id AS relationship,
           link_order,
           lrs.link,
           COALESCE(text_value, '') AS text_value
    FROM l_event_series lrs
    JOIN series s ON s.id = lrs.entity1
    JOIN link l ON l.id = lrs.link
    JOIN link_type lt ON (lt.id = l.link_type AND lt.gid = '707d947d-9563-328a-9a7d-0c5b9c3a9791')
    LEFT OUTER JOIN link_attribute_text_value latv ON (latv.attribute_type = 788 AND latv.link = l.id)
    ORDER BY series, link_order;

CREATE OR REPLACE VIEW recording_series AS
    SELECT entity0 AS recording,
           entity1 AS series,
           lrs.id AS relationship,
           link_order,
           lrs.link,
           COALESCE(text_value, '') AS text_value
    FROM l_recording_series lrs
    JOIN series s ON s.id = lrs.entity1
    JOIN link l ON l.id = lrs.link
    JOIN link_type lt ON (lt.id = l.link_type AND lt.gid = 'ea6f0698-6782-30d6-b16d-293081b66774')
    LEFT OUTER JOIN link_attribute_text_value latv ON (latv.attribute_type = 788 AND latv.link = l.id)
    ORDER BY series, link_order;

CREATE OR REPLACE VIEW release_series AS
    SELECT entity0 AS release,
           entity1 AS series,
           lrs.id AS relationship,
           link_order,
           lrs.link,
           COALESCE(text_value, '') AS text_value
    FROM l_release_series lrs
    JOIN series s ON s.id = lrs.entity1
    JOIN link l ON l.id = lrs.link
    JOIN link_type lt ON (lt.id = l.link_type AND lt.gid = '3fa29f01-8e13-3e49-9b0a-ad212aa2f81d')
    LEFT OUTER JOIN link_attribute_text_value latv ON (latv.attribute_type = 788 AND latv.link = l.id)
    ORDER BY series, link_order;

CREATE OR REPLACE VIEW release_group_series AS
    SELECT entity0 AS release_group,
           entity1 AS series,
           lrgs.id AS relationship,
           link_order,
           lrgs.link,
           COALESCE(text_value, '') AS text_value
    FROM l_release_group_series lrgs
    JOIN series s ON s.id = lrgs.entity1
    JOIN link l ON l.id = lrgs.link
    JOIN link_type lt ON (lt.id = l.link_type AND lt.gid = '01018437-91d8-36b9-bf89-3f885d53b5bd')
    LEFT OUTER JOIN link_attribute_text_value latv ON (latv.attribute_type = 788 AND latv.link = l.id)
    ORDER BY series, link_order;

CREATE OR REPLACE VIEW work_series AS
    SELECT entity1 AS work,
           entity0 AS series,
           lsw.id AS relationship,
           link_order,
           lsw.link,
           COALESCE(text_value, '') AS text_value
    FROM l_series_work lsw
    JOIN series s ON s.id = lsw.entity0
    JOIN link l ON l.id = lsw.link
    JOIN link_type lt ON (lt.id = l.link_type AND lt.gid = 'b0d44366-cdf0-3acb-bee6-0f65a77a6ef0')
    LEFT OUTER JOIN link_attribute_text_value latv ON (latv.attribute_type = 788 AND latv.link = l.id)
    ORDER BY series, link_order;

CREATE OR REPLACE VIEW medium_track_durations AS
    SELECT
        medium.id AS medium,
        array_agg(track.length ORDER BY track.position) FILTER (WHERE track.position = 0) AS pregap_length,
        array_agg(track.length ORDER BY track.position) FILTER (WHERE track.position > 0 AND track.is_data_track = false) AS cdtoc_track_lengths,
        array_agg(track.length ORDER BY track.position) FILTER (WHERE track.is_data_track = true) AS data_track_lengths
    FROM medium
    JOIN track ON track.medium = medium.id
    GROUP BY medium.id;

COMMIT;

-- vi: set ts=4 sw=4 et :
