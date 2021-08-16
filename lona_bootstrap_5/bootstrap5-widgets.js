function Bootstrap5Modal(lona_window) {
    this.lona_window = lona_window;

    this._update = function() {
        if(this.data.visible) {
            this.modal.show();
        } else {
            this.modal.hide();
        };
    };

    this.setup = function() {
        this.modal = new bootstrap.Modal(
            this.nodes[0],
            this.data.modal_options,
        );

        this._update();
    };

    this.data_updated = function() {
        this._update();
    };
};

Lona.register_widget_class('lona_bootstrap5.Modal', Bootstrap5Modal);