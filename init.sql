CREATE TABLE IF NOT EXISTS commodity(
 brand TEXT PRIMARY KEY NOT NULL,
 cost int NOT NULL
);
CREATE TABLE IF NOT EXISTS sale(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 commodity_brand TEXT NOT NULL,
 price INTEGER NOT NULL,
 cost INTEGER NOT NULL,
 created_at INT NOT NULL DEFAULT (strftime('%s', 'now')),
 FOREIGN KEY (commodity_brand) REFERENCES commodity(brand)
);
