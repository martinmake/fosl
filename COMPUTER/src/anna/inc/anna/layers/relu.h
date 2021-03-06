#ifndef _ANNA_LAYER_RELU_H_
#define _ANNA_LAYER_RELU_H_

#include <inttypes.h>

#include "anna/layers/base.h"

namespace Anna
{
	namespace Layer
	{
		class Relu final : public Base
		{
			public: // STATIC VARIABLES
				static const std::string NAME;
				static const bool        CHANGES_DATA_SHAPE;
				static const bool        IS_INPUT;
				static const bool        IS_OUTPUT;
				static const bool        HAS_TRAINABLE_PARAMETERS;

			public: // CONSTRUCTORS AND DESTRUCTOR
				Relu(Shape initial_output_shape = Shape::INVALID);
				~Relu(void);

			public:
				void  forward(const std::list<std::shared_ptr<Base>>::        iterator& current_layer                     ) override;
				void backward(const std::list<std::shared_ptr<Base>>::reverse_iterator& current_layer, bool update_weights) override;

			private:
				void activate(void);
				void calculate_error_back(Tensor& error_back) const;

			public: // GETTERS FOR STATIC VARIABLES
				const std::string& name                    (void) const override;
				      bool         changes_data_shape      (void) const override;
				      bool         is_input                (void) const override;
				      bool         is_output               (void) const override;
				      bool         has_trainable_parameters(void) const override;
		};

		// GETTERS FOR STATIC VARIABLES
		inline const std::string& Relu::name                    (void) const { return NAME;                     }
		inline       bool         Relu::changes_data_shape      (void) const { return CHANGES_DATA_SHAPE;       }
		inline       bool         Relu::is_input                (void) const { return IS_INPUT;                 }
		inline       bool         Relu::is_output               (void) const { return IS_OUTPUT;                }
		inline       bool         Relu::has_trainable_parameters(void) const { return HAS_TRAINABLE_PARAMETERS; }
	}
}

#endif
