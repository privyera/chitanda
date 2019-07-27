CREATE TABLE tells (
    id INTEGER,
    channel TEXT NOT NULL,
    listener TEXT NOT NULL,
    message TEXT NOT NULL,
    time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    recipient TEXT NOT NULL,
    sender TEXT NOT NULL,
    PRIMARY KEY (id)
);