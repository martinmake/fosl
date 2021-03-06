#ifndef _GRA_INPUT_WINDOW_BASE_H_
#define _GRA_INPUT_WINDOW_BASE_H_

#include <string>

#include <sml/sml.h>

#include "gra/core.h"
#include "gra/inputs/base.h"

namespace Gra
{
	namespace Input
	{
		namespace Window
		{
			class Base : public Input::Base
			{
				protected:
					Base(void);

				public:
					enum class Action
					{
						PRESS   = GLFW_PRESS,
						RELEASE = GLFW_RELEASE,
					};
					enum class Mod
					{
						SHIFT     = GLFW_MOD_SHIFT,
						CONTROL   = GLFW_MOD_CONTROL,
						ALT       = GLFW_MOD_ALT,
						SUPER     = GLFW_MOD_SUPER,
						CAPS_LOCK = GLFW_MOD_CAPS_LOCK,
						NUM_LOCK  = GLFW_MOD_NUM_LOCK,
					};

				DECLARATION_MANDATORY_INTERFACE(Base)
			};

			DEFINITION_MANDATORY(Base, )
		}
	}
}

#endif
