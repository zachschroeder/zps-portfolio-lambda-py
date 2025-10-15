class MovieAuditProjection:

    def handle_event(self, event):
        print("Audit Event Received: ", event)
