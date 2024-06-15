CREATE TABLE "message"(
    "id" BIGINT NOT NULL,
    "user_id" BIGINT NOT NULL,
    "content" TEXT NOT NULL,
    "created" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "deleted" BOOLEAN NULL
);
ALTER TABLE
    "message" ADD PRIMARY KEY("id");
CREATE TABLE "comment"(
    "id" BIGINT NOT NULL,
    "post_id" BIGINT NOT NULL,
    "user_id" BIGINT NOT NULL,
    "content" TEXT NOT NULL,
    "created" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "deleted" BOOLEAN NULL
);
ALTER TABLE
    "comment" ADD PRIMARY KEY("id");
CREATE TABLE "post"(
    "id" BIGINT NOT NULL,
    "user_id" BIGINT NOT NULL,
    "content" TEXT NOT NULL,
    "created" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "deleted" BOOLEAN NULL
);
ALTER TABLE
    "post" ADD PRIMARY KEY("id");
CREATE TABLE "user"(
    "id" BIGINT NOT NULL,
    "username" VARCHAR(255) NOT NULL,
    "fullname" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL,
    "user_details" JSON NULL,
    "user_settings" JSON NULL,
    "closed" BOOLEAN NULL
);
ALTER TABLE
    "user" ADD PRIMARY KEY("id");
ALTER TABLE
    "message" ADD CONSTRAINT "message_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "user"("id");
ALTER TABLE
    "comment" ADD CONSTRAINT "comment_post_id_foreign" FOREIGN KEY("post_id") REFERENCES "post"("id");
ALTER TABLE
    "post" ADD CONSTRAINT "post_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "user"("id");
ALTER TABLE
    "comment" ADD CONSTRAINT "comment_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "user"("id");