-- Write sql script

CREATE TRIGGER decrease_items_quantity AFTER INSERT ON orders FOR EACH ROW
UPDATE item SET quantity = quantity - NEW.number WHERE name=NEW.item_name;
