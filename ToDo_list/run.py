from views.main import main_window
from db.db_init import iniciar_db

iniciar_db()
main_window.mainloop()